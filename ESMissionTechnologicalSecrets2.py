import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import ESPanel as panel

def run():
	print '--> mission Technological Secrets (2 of 3)'

	# # this is a transport mission
	# if not (station.openInventory() \
	# 	and station.loadItem('img/dna_sample.bmp') \
	# 	and station.closeInventory()):
	# 	return False

	# if not station.undock():
	# 	return False

	# pilot.autopilot()

	# if not space.setMissionWaypoint():
	# 	return False
		
	print '<-- mission Technological Secrets (2 of 3)\n'
	return True
