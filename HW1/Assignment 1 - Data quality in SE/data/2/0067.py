import ROOT
from ROOT import TCanvas, TGraph
from ROOTDefs import get_po_signal_et_background_files
from ROCCurveDefs import create_roc_counter, roc_efficiencies_from_cuts
from tqdm import tqdm
import numpy as np

'''
Manually "train" weights to minimize the background efficiency at 90% signal efficiency. Not using a neural network
module because they cannot train on this directly.
'''

c1 = TCanvas("c1", "Graph Draw Options", 200, 10, 600, 400)

tsig, fsig, tback, fback = get_po_signal_et_background_files()

netcuts = 100

init_weights = [1, 1, 1, 1, 1]
l0_weight_range = [i*0.1 for i in range(21)]
efficiencies = []
print(l0_weight_range)

for l0_weight in tqdm(l0_weight_range):
    new_weights = [l0_weight, 1, 1, 1, 1]
    tsig.set_reco_et_layer_weights(new_weights)
    tback.set_reco_et_layer_weights(new_weights)

    sig_cuts = create_roc_counter(tsig, netcuts, -20, 100, 0)
    back_cuts = create_roc_counter(tback, netcuts, -20, 100, 0)

    sig_eff, back_eff = roc_efficiencies_from_cuts(sig_cuts, back_cuts)

    for i in range(netcuts):
        if sig_eff[i] < 0.9:
            print(l0_weight)
            print(back_eff[i])
            efficiencies.append(back_eff[i])
            break

l0_weight_range = np.array(l0_weight_range)
efficiencies = np.array(efficiencies)

gr = TGraph(11, l0_weight_range, efficiencies)
gr.SetTitle('Background Efficiency (@ 90% Signal Efficiency) vs. L0 Weights')
gr.GetXaxis().SetTitle('L0 Weight')
gr.GetYaxis().SetTitle('Background Eff')
gr.Draw('A*')

c1.Print('ManualTester0-2.pdf')