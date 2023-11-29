# scalebar-o-matic version 2 by connor garrels, 2023 CE

# Add a 100nm scale bar to all images in source directory and save them to a new subdirectory. 

import os
from ij import IJ
from ij.gui import GenericDialog
from ij.io import FileSaver

# make GUI and variables
gui = GenericDialog("scalebar-o-matic_v2")

gui.addMessage("<html><b> Source Directory </html></b>")
gui.addDirectoryField("Source Directory", "")

gui.addMessage("<html><b> Set Scale </b></html>")
gui.addNumericField("Pixel Size (A/px) ", 0, 3)

gui.addHelp("https://ohsuitg-my.sharepoint.com/:x:/g/personal/reichow_ohsu_edu/EdWSYq_CUidLn1gHWf5GRFcB3q9LWCfj-dEXM4sChd7CdQ?e=yNnIvw")
gui.setHelpLabel("What's my pixel size?")

gui.showDialog()

# Don't fucking touch this it's washed
def bar_o_lyzer(imp, pixel_size):
	IJ.run(imp, "Set Scale...", "distance = 1 known = pixel_size unit = Å global")
	IJ.run(imp, "Scale Bar...", "width=1000 thickness=50 font = [] color=White background=None location=[Lower Right] horizontal hide")

def rename_and_save(imp):
	split = filename.split(".")
	stem = split[0]
	FileSaver(imp).saveAsTiff(target_dir + '/' + stem + '_scalebar.TIF')
		
if gui.wasOKed():
	source_dir = gui.getNextString()
	pixel_size = gui.getNextNumber()
	
	target_dir =(source_dir + 'scale_bar') 
	os.mkdir(target_dir)
	
	for filename in os.listdir(source_dir):
		if filename.endswith(".TIF"):
			print "Bar-o-lyzing", filename
			imp = IJ.openImage(os.path.join(source_dir, filename))
			if imp is None:
				print "Could not open image", filename
				continue
			bar_o_lyzer(imp, pixel_size)
			rename_and_save(imp)
		else:
			print "Ignoring", filename
	print('Done.')
