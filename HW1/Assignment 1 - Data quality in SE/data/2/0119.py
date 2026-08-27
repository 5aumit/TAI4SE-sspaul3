import taso
import onnx

import torch
import torch.nn as nn
import torchvision.models as models

class SampleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3,3,3,padding=1)
        self.conv2 = nn.Conv2d(3,3,3,padding=1)
        self.relu = nn.ReLU()

    def forward(self,X):
        x = self.conv1(X)
        x = self.conv1(x)
        x = self.relu(x)

        y = self.conv2(X)
        y = self.conv2(y)
        y = self.relu(y)

        x = x+y
        x = x+1
        x = x+3
        # x = x * 2
        # x = x * 0.5

        return x

model = SampleModel()
x = torch.randn(1, 3, 24, 24, device='cpu')
torch.onnx.export(model,
    x,
    "model.onnx",
    verbose=False,)
graph = taso.load_onnx("./model.onnx")
print("\n cost = {}".format(graph.cost()))
new_graph = taso.optimize(graph, alpha = 1.0, budget = 1000, print_subst=True)
print("\n optimized_cost = {}".format(new_graph.cost()))
new_model = taso.export_onnx(new_graph)
onnx.save(new_model, "./model_taso.onnx")