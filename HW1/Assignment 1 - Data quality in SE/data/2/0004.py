def gen_metadata(fn):
	metadata = {}
	lines = open(fn,'r').readlines()
	for line in lines:
		line = line.rstrip()
		if len(line) == 0:
			continue
		elif line.startswith('#'):
			continue
		elif line.startswith('%'):
			continue
		else:
			# Special case RingThresh
			firstWord = line.split()[0]
			if line.startswith('RingThresh'):
				if 'RingThresh' not in metadata.keys():
					metadata.update({'RingThresh':{}})
				strippedline = line.split(firstWord)[1].strip()
				secondword = strippedline.split()[0]
				metadata['RingThresh'].update({secondword:strippedline.split(secondword)[1].split('#')[0].strip()})
			else:
				metadata.update({firstWord : line.split(firstWord)[1].split('#')[0].strip()})
	return metadata

def SetupPayloads(inp):
	flow_input = {
		"input": {
			"inject_source_endpoint_id":		inp['sourceEP'],
			"funcx_endpoint_non_compute":		inp['sourceNCEP'],
			"proc_endpoint_non_compute":		inp['procNCEP'],
			"inject_source_path":				inp['sourcePath'],
			"inject_destination_endpoint_id":	inp['remoteDataEP'],
			"extract_source_endpoint_id":		inp['remoteDataEP'],
			"funcx_endpoint_compute":			inp['funcx_endpoint_compute'],
			"inject_destination_path":			inp['executePath'],
			"extract_source_path":				inp['executeResultPath'],
			"extract_destination_endpoint_id":	inp['destEP'],
			"extract_destination_path":			inp['resultPath'],
			"paramFileName":					inp['pfName'],
			"startLayerNr":						inp['startLayerNr'],
			"endLayerNr":						inp['endLayerNr'],
			"nFrames":							inp['nFrames'],
			"numProcs":							inp['numProcs'],
			"numBlocks":						inp['numBlocks'],
			"timePath":							inp['timePath'],
			"StartFileNrFirstLayer":			inp['startNrFirstLayer'],
			"NrFilesPerSweep":					inp['nrFilesPerSweep'],
			"FileStem":							inp['fileStem'],
			"SeedFolder":						inp['seedFolder'],
			"RawFolder":						inp['rawFolder'],
			"darkFN":							inp['darkFN'],
			"StartNr":							inp['startNr'],
			"EndNr":							inp['endNr'],
			'extract_recursive':				False,
			'inject_recursive':					True,}
		}
	flow_input['input'].update({
			'multipletasks':[{
				'startLayerNr':inp['startLayerNr'],
				'endLayerNr':inp['endLayerNr'],
				'numProcs':inp['numProcs'],
				'nFrames':inp['nFrames'],
				'numBlocks':inp['numBlocks'],
				'blockNr':idx,
				'timePath':inp['timePath'],
				'FileStem':inp['fileStem'],
				'SeedFolder':inp['seedFolder'],
				'RawFolder':inp['rawFolder'],
				'paramFileName':inp['pfName'],
				}
			for idx in range(inp['numBlocks'])
		]
	})
	flow_input['input'].update({
		'pilot':{
			'dataset':f'{inp["sourcePath"]}/{inp["fileStem"]}_Layer_{str(inp["startLayerNr"]).zfill(4)}_Analysis_Time_{inp["timePath"]}/{inp["fileStem"]}_Layer_{str(inp["startLayerNr"]).zfill(4)}_Analysis_Time_{inp["timePath"]}/',
			'index':inp['portal_id'],
			'project':'hedm',
			'source_globus_endpoint':inp['sourceEP'],
		}
	})
	
	flow_input['input']['pilot'].update({
		'metadata':gen_metadata(inp['pfName']),
	})
	flow_input['input']['pilot']['metadata'].update({
		'exp_id':f'{inp["experimentName"]}_{inp["fileStem"]}_{inp["timePath"]}',
	})
	flow_input['input']['pilot']['metadata'].update({
		'time_path':inp["timePath"],
	})
	flow_input['input']['pilot']['metadata'].update({
		'startNr':inp["startNr"],
		'endNr':inp["endNr"],
	})
	return flow_input
