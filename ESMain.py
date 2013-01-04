import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESPanel as panel
import ESStation as station
import ESShortcut as sc

def inStation():
    x, y = image.findImgR(panel.Menu,
        'img/undock.bmp', 0.2)
    if x > 0 and y > 0:
        return True
    return False

bots = {}

def run():
    if not inStation():
        print 'Error: Must begin at station.'
        return

    agent = 'img/agent.bmp'
    print 'mission bot begin.'
    while True:

        # if not station.startConversation(agent):
        #     print 'Error: Could not find target agent.'
        #     return

        mission = image.extractTextR(panel.MissionName).strip()
        if mission not in bots:
            print 'Error: Cant find bot for mission \'' + mission + '\'.'
            return

        bot = bots[mission]

        # TODO
        break

if __name__ == '__main__':
    run()