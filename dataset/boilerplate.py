def test_with_filters(
    clf = RandomForestClassifier(n_estimators=100, class_weight='balanced', n_jobs=-1),
    features_selection = df_features.columns,
    genres_filter = [True] * len(df_genres),
    feature_filter = [True] * len(df_features),
    midis_treshold=2500,
    drop_duplicates=True,
    repartition=True,
    normalize_conf_matrix=True):
    
    
    df_pred = df_genres[genres_filter][['genre']].join(df_features[features_selection][feature_filter], how='inner').reset_index()
    df_pred = df_pred.replace([np.inf, -np.inf], np.nan).dropna()
    df_pred.head()

    df_counts = df_pred.groupby('genre').size().reset_index(name='counts').sort_values(by='counts', ascending=False)
    df_pred_sel = df_pred[df_pred.genre.isin(df_counts[df_counts.counts > midis_treshold]['genre'])]
    if drop_duplicates:
        df_pred_sel = df_pred_sel[~df_pred_sel['file_name'].duplicated(keep=False)]
    print("%d genres entailing %d MIDIs will be considered."%(len(np.unique(df_pred_sel['genre'])), len(df_pred_sel)))
    print('The genres are: %s'%", ".join(np.unique(df_pred_sel['genre'])))

    print("%.3f%% of the midis are duplicates"%((len(df_pred_sel)-df_pred_sel['file_name'].nunique())/len(df_pred_sel)*100))
    
    scaler = StandardScaler()
    X = scaler.fit_transform(df_pred_sel.iloc[:, 2:])
    y, labels = pd.factorize(df_pred_sel['genre'])
    
    skf = RepeatedStratifiedKFold(n_splits=5, n_repeats=5)
    
    scores = {'train_accuracy': [], 'test_accuracy': []}
    feature_importances = []
    
    binary = len(labels) == 2
    if binary:
        scores['train_f1'] = []
        scores['test_f1'] = []
        scores['train_rocauc'] = []
        scores['test_rocauc'] = []
    
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        feature_importances.append(clf.feature_importances_)
        scores['train_accuracy'].append(clf.score(X_train, y_train))
        scores['test_accuracy'].append(clf.score(X_test, y_test))
        if binary:
            train_pred = clf.predict(X_train)
            test_pred = clf.predict(X_test)
            scores['train_f1'].append(f1_score(y_train, train_pred))
            scores['test_f1'].append(f1_score(y_test, test_pred))
            scores['train_rocauc'].append(roc_auc_score(y_train, train_pred))
            scores['test_rocauc'].append(roc_auc_score(y_test, test_pred))
    
    for key, score in scores.items():
        scores[key] = np.array(scores[key])
    
    if repartition:
        val, counts_dataset = np.unique(y, return_counts=True)
        display(pd.DataFrame([counts_dataset/counts_dataset.sum()], columns=[labels[i] for i in val], index=['Repartition']))
    
    index = [['accuracy', 'accuracy'],['mean', 'std']]
    if binary:
        index[0].extend(['f1', 'f1', 'rocauc', 'rocauc'])
        index[1].extend(['mean', 'std', 'mean', 'std'])
    
    results = []
    
    for idx, measure in enumerate(np.array(index[0])[::2]):
        results.append([])
        results.append([])
        idx *= 2
        results[idx].append("%.2f%%"%(scores['train_'+ measure].mean()*100))
        results[idx+1].append("%.2f%%"%(scores['train_'+ measure].std()*100))
        results[idx].append("%.2f%%"%(scores['test_' + measure].mean()*100))
        results[idx+1].append("%.2f%%"%(scores['test_' + measure].std()*100))
    display(pd.DataFrame(results, columns=['Train', 'Test'], index=index))
    
    pred = cross_val_predict(clf, X, y, cv=5)
    arr = confusion_matrix(y, pred)
    if normalize_conf_matrix:
        arr = arr/arr.sum(axis=1).reshape(1,-1).T*100
    df_cm = pd.DataFrame(arr, index = [i for i in labels],
                         columns = [i for i in labels])
    plt.figure(figsize = (10,7))

    sns.heatmap(df_cm, annot=True, cmap='Blues', fmt='.2f')
    plt.xlabel("Predicted class")
    plt.ylabel("Actual class")
    plt.title("Confusion matrix for random forest classification")
    plt.show();
    return scores, feature_importances, pred

def get_most_common_in_top(features_importance, top=25):
    features_importance = np.array(features_importance)
    max_features = features_importance.argsort(axis=1)[:, ::-1]

    estimate_importance = features_importance.mean(axis=0)
    idx2score = dict(zip(np.arange(df_features.shape[1]), estimate_importance)).get

    a = max_features[:,:top]
    feature_selection = set(np.arange(df_features.shape[1]))

    for i in range(len(a)):
        feature_selection.intersection_update(set(a[i]))
    features_sorted = (np.array(list(feature_selection))
                       [np.array(list(map(idx2score, list(feature_selection)))).argsort()[::-1]])
    return features_sorted, np.array(list(map(idx2score, features_sorted)))

