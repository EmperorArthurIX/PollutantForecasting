---

| Model Name      | Description                                     | Limitations      | Accuracy  |
|-----------------|-------------------------------------------------|---------------|----------------|
| LSTM   | Long Short Term Memory    | Limited to 4 variable Predictions | 2 hours |
| Bi-LSTM | BiDirectional Long Short Term Memory | Lower Conversion Rate | 30 minutes |
| Iterative CNN | Involves iterative feedback loops between different CNN layers, allowing for refined feature extraction in each iteration | Overfitted easily | 4 hours  |
| Integrated CNN     | Incorporates multiple types of data into a single unified CNN architecture to extract combined and complementary features. | Overfitted easily         | 1 hour         |
| Extra Tree Regressor (PyCaret)   | Inbuilt model that performed better than the pre-existing 25 models | No Pruning of Tree is allowed | 3 hours        |
| Extra Tree Regressor (Ensemble)   | decision tree-based regression model, resulting in an ensemble of highly randomized trees for improved prediction accuracy. | Currently Lacks Refinement           | 3 hours        |


---