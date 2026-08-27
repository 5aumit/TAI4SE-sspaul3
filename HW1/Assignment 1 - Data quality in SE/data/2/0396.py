import sys, os
from db.interface import *
from learning import interface
from analysis import graphutils
from learning import consolidateFeatures
from mlabwrap import mlab
import numpy as np
import datetime

LEARNING_ROOT="learning/"
FEATURES="features"
LABELS="ytrain"

def main(args):
	db = args[0]
	date1 = args[1]
	date2 = args[2]
	date3 = args[3]
	k = int(args[4])
	basename = args[5]

	reader = DBReader(db)
	print("Getting uid")
	uid = reader.uid()

	print("Getting all the feature graphs")
	feature_graphs = graphutils.get_feat_graphs(db, uid, None, date2)

	print("Getting Gcollab_delta graph")
	Gcollab_delta = graphutils.get_collab_graph(db, uid, date1, date2)
	Gcollab_base = graphutils.get_collab_graph(db, uid, date3, date1)

	base_graphs = graphutils.get_base_dict(Gcollab_base, feature_graphs)
	graphutils.print_stats(base_graphs)
	graphutils.print_graph_stats("Gcollab_delta", Gcollab_delta)

	filepath = os.path.join(LEARNING_ROOT, basename + ".mat")
	features_matrix_name = "%s_%s"%(basename, FEATURES)
	labels_matrix_name = "%s_%s"%(basename, LABELS)

	features = consolidateFeatures.consolidate_features_add(base_graphs, k, Gcollab_delta)
	#features = consolidateFeatures.consolidate_features(base_graphs, Gcollab_delta, k)
	labels = consolidateFeatures.consolidate_labels(features, Gcollab_delta)

	np_train, np_output = interface.matwrapTrain(features, labels)
	interface.writeTrain(np_train, np_output, filepath, features_matrix_name, labels_matrix_name)	
	
	# Add learning root to mlab path so that all .m functions are available as mlab attributes
	mlab.path(mlab.path(), LEARNING_ROOT)	
	mlab.training(np_train, np_output)

# NOTE base graph = till date3 to date1
# delta graph = date1 to date2
# This file calls consolidate_features for the base graph, consolidate_labels for the delta graph and writes the .mat file
# based on the basename. It also needs the k (number of hops) parameter
if __name__=="__main__":
	if len(sys.argv)<6:
		print("Usage: program.py <db> <date1> <date2> <date3> <k hops> <basename mat>")
		sys.exit(1)
	
	main(sys.argv[1:])
