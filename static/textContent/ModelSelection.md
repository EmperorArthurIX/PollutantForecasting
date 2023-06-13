---

| Model Name      | Description                                     | Limitations      | RMSE  | R2 |
|-----------------|-------------------------------------------------|---------------|----------|---------|
| LSTM   | Long Short Term Memory    | Limited to single variable dependency | 18 | 0.95 |
| Bi-LSTM | BiDirectional Long Short Term Memory | Limited to single variable dependency | 18 | 0.96 |
| Iterative CNN | Involves iterative feedback loops between different CNN layers, allowing for refined feature extraction in each iteration | Overfitted easily | 16  | 0.9 |
| Integrated CNN     | Incorporates multiple types of data into a single unified CNN architecture to extract combined and complementary features. | Overfitted easily         | 24         |0.92|
| Extra Tree Regressor (PyCaret)   | Inbuilt model that performed better than the pre-existing 25 models | Manual Pruning of Tree is not allowed | 40        | 0.93 |
| Extra Tree Regressor (Ensemble)   | decision tree-based regression model, resulting in an ensemble of highly randomized trees for improved prediction accuracy. | Prone to overfitting unless rigorously pruned         | 20 |0.93|


---