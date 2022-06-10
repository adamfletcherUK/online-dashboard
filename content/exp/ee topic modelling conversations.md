### Topic Modelling Call Centre Transcripts to Determine Common Conversations

The client had a large amount of call centre transcripts and wanted to improve their service speed to customers,
improving satisfaction.

- The main goal of the project was to surface common questions customers had to increase the speed of the customer being
  given the knowledge they were seeking.
- To accomplish this task I embedded the text using a BERT model, turning the sentence into a vector.
- I then used UMAP to reduce the dimensionality of the word-embeddings.
    - UMAP was chosen as it is non-linear so my rationale was that it was better suited for use with transformers than
      PCA.
- I then performed clustering to group the individual call centre transcripts together.
    - I used HDBScan and kmeans for clustering.
    - HDBScan has advantages in that it doesn't need to be given the number of clusters to make (k) and it also makes
      an "un-clustered" cluster, a disadvantage was that I couldn't get the clustering to be deterministic - making
      repeatability an issue
    - k-means clustering requires a number of clusters to be specified, reducing automation potential (although we can
      employ methods to circumvent this), however, the clustering patterning was better than HDBScan.
- From these clusters I was able to generate common questions, topics and phrases which customers required.
    - This was conducted using tf-idf and n-gram analysis of the clusters (and also sub-clusters of the above clusters)
- The business is now able to look at common questions, topics at different hierarchies and can surface more specific
  information to customers faster.