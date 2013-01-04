import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space

def run():
	print '--> mission Gone Berserk'

	if not station.undock():
		return False

	print '<-- mission Gone Berserk\n'
	return True
