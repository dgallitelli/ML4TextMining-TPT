"""
=======================================================================================
Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation
=======================================================================================

This is an example of applying :class:`sklearn.decomposition.NMF` and
:class:`sklearn.decomposition.LatentDirichletAllocation` on a corpus
of documents and extract additive models of the topic structure of the
corpus.  The output is a list of topics, each represented as a list of
terms (weights are not shown).

Non-negative Matrix Factorization is applied with two different objective
functions: the Frobenius norm, and the generalized Kullback-Leibler divergence.
The latter is equivalent to Probabilistic Latent Semantic Indexing.

The default parameters (n_samples / n_features / n_components) should make
the example runnable in a couple of tens of seconds. You can try to
increase the dimensions of the problem, but be aware that the time
complexity is polynomial in NMF. In LDA, the time complexity is
proportional to (n_samples * iterations).

"""

# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck
#         Chyi-Kwei Yau <chyikwei.yau@gmail.com>
# License: BSD 3 clause

from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()


# Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
# to filter out useless terms early on: the posts are stripped of headers,
# footers and quoted replies, and common English words, words occurring in
# only one document or in at least 95% of the documents are removed.
def run_example(_random_state, _beta_loss=None, _vectorizer=None, _init=None, _W=None, _H=None):
    n_samples = 2000
    n_features = 1000
    n_components = 10
    n_top_words = 20
    
    # =============================
    # Setting up the dataset
    # =============================

    print("Loading dataset...")
    t0 = time()
    dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                                 remove=('headers', 'footers', 'quotes'))
    data_samples = dataset.data[:n_samples]
    print("done in %0.3fs." % (time() - t0))
    
    if _vectorizer is None:
        # Use tf-idf features for NMF.
        print("Extracting tf-idf features for NMF...")
        vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                       max_features=n_features,
                                       stop_words='english')
    else:
        # Use CountVectorizer features for NMF.
        print("Extracting CountVectorizer features for NMF...")
        vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                       max_features=n_features,
                                       stop_words='english')        
    t0 = time()
    features = vectorizer.fit_transform(data_samples)
    print("done in %0.3fs." % (time() - t0))
    
    # =============================
    
    
    # =============================
    # Building the NMF Model
    # =============================
    
    # Fit the NMF model
    vect_string = _vectorizer if _vectorizer != None else "tf-idf"
    beta_loss_string = _beta_loss if _beta_loss != None else "Frobenius"
    
    print("Fitting the NMF model ("+beta_loss_string+" norm) with "+vect_string+" features, "
          "n_samples=%d and n_features=%d..."
          % (n_samples, n_features))
    t0 = time()
    if _beta_loss is None:
        if _init is None:
            nmf = NMF(n_components=n_components, random_state=_random_state,
                      alpha=.1, l1_ratio=.5).fit(features)
        else:
            nmf = NMF(n_components=n_components, random_state=_random_state,
                      alpha=.1, l1_ratio=.5, init=_init).fit_transform(features, W=_W, H=_H)           
    else:
        if _init is None:
            nmf = NMF(n_components=n_components, random_state=_random_state,
                      alpha=.1, l1_ratio=.5, solver='mu', beta_loss=_beta_loss).fit(features)
        else:
            nmf = NMF(n_components=n_components, random_state=_random_state,
                      alpha=.1, l1_ratio=.5, solver='mu', beta_loss=_beta_loss,
                      init=_init).fit_transform(features, W=_W, H=_H)
    print("done in %0.3fs." % (time() - t0))

    print("\nTopics in NMF model ("+beta_loss_string+" norm):")
    feature_names = vectorizer.get_feature_names()
    print_top_words(nmf, feature_names, n_top_words)
    
    # =============================
    
    
    # =============================
    # Building the NMF Model with LDA
    # =============================

    # Use tf (raw term count) features for LDA.
    # print("Extracting tf features for LDA...")
    # tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
    #                                 max_features=n_features,
    #                                 stop_words='english')
    # t0 = time()
    # tf = tf_vectorizer.fit_transform(data_samples)
    # print("done in %0.3fs." % (time() - t0))
    # print()

# 
    # # Fit the NMF model
    # print("Fitting the NMF model (generalized Kullback-Leibler divergence) with "
    #       "tf-idf features, n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))
    # t0 = time()
    # nmf = NMF(n_components=n_components, random_state=_random_state,
    #           beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
    #           l1_ratio=.5).fit(tfidf)
    # print("done in %0.3fs." % (time() - t0))

    # print("\nTopics in NMF model (generalized Kullback-Leibler divergence):")
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # print_top_words(nmf, tfidf_feature_names, n_top_words)

    # print("Fitting LDA models with tf features, "
    #       "n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))
    # lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
    #                                 learning_method='online',
    #                                 learning_offset=50.,
    #                                 random_state=0)
    # t0 = time()
    # lda.fit(tf)
    # print("done in %0.3fs." % (time() - t0))

    # print("\nTopics in LDA model:")
    # tf_feature_names = tf_vectorizer.get_feature_names()
    # print_top_words(lda, tf_feature_names, n_top_words)
