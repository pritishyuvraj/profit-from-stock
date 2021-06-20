import torch
import torch.nn as nn
import numpy as np

class LSTM(nn.Module):
    def __init__(self, input_size=3000, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (
            torch.zeros(1, 1, self.hidden_layer_size),
            torch.zeros(1, 1, self.hidden_layer_size),
        )

    def forward(self, input_seq):
        input_seq = torch.Tensor(input_seq)
        lstm_out, self.hidden_cell = self.lstm(
            input_seq.view(len(input_seq), 1, -1), self.hidden_cell
        )
        print("input dimension", input_seq.view(len(input_seq), 1, -1).shape)
        print("lstm shape", lstm_out.shape)
        print("hidden cell", np.ndim(self.hidden_cell))
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

if __name__ == '__main__':
    model = LSTM()
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    print(model)

    # Random Data
    dummy_data = np.random.randint(1, 5, size=(100,3000))
    dummy_values = np.random.randint(1, 10, size=(10))
    dummy_pred = model(dummy_data)
    print(dummy_pred)
    print(dummy_pred.shape)
