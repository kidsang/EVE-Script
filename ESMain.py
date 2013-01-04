import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESPanel as panel
import ESStation as station
import ESSpace as space
import ESShortcut as sc

import ESMissionGoneBerserk as gone_berserk

def inStation():
    x, y = image.findImgR(panel.Menu,
        'img/undock.bmp', 0.2)
    if x > 0 and y > 0:
        return True
    return False

bots = {'Gone Berserk':gone_berserk}

def run():
    # if not inStation():
    #     print 'Error: Must begin at station.'
    #     return

    # agent = 'img/agent.bmp'
    # print 'mission bot begin. \n'
    # while True:

    #     if not station.startConversation(agent):
    #         print 'Error: Could not find target agent.'
    #         return

    #     mission = image.extractTextR(panel.MissionName).strip()
    #     if mission not in bots:
    #         print 'Error: Cant find bot for mission \'' + mission + '\'.'
    #         return
    #     bot = bots[if not mission]:

    #     if not station.acceptMission():
    #         print 'Error: Accept mission failed.'
    #         return

        # TODO:test
        bot = bots['Gone Berserk']

        # TODO:test
        mouse.moveTo(1000, 100)
        mouse.leftClick()

        if not space.setMissionWaypoint():
            print 'Error: Cant set mission waypoint.'
            return

        if not bot.run():
            print 'Error: Mission abort.'

        # TODO
        # break

if __name__ == '__main__':
    run()