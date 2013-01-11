import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESPanel as panel
import ESStation as station
import ESSpace as space
import ESShortcut as sc
import ESPilot as pilot

import ESMissionGoneBerserk as gone_berserk
import ESMissionTheDrugBust as the_drug_bust
import ESMissionUnauthorizedMilitaryPresence as unauthorized_military_presence
import ESMissionAvengeAFallenComrade as avenge_a_fallen_comrade
import ESMissionCustomsInterdictian1 as customs_interdictian_1
import ESMissionCustomsInterdictian2 as customs_interdictian_2
import ESMissionDeadlyArrival as deadly_arrival
import ESMissionLaborsOfWar1 as labors_of_war_1
import ESMissionLaborsOfWar2 as labors_of_war_2
import ESMissionLaborsOfWar3 as labors_of_war_3
import ESMissionPirateIntrusion as pirate_intrusion
import ESMissionTheHiddenStash as the_hidden_stash
import ESMissionMissionOfMercy as mission_of_mercy
import ESMissionRecon1 as recon_1
import ESMissionRecon2 as recon_2
import ESMissionRecon3 as recon_3
import ESMissionTheDamselInDistress as the_damsel_in_distress
import ESMissionTheSanshaSpies as the_sansha_spies
import ESMissionTechnologicalSecrets1 as technological_secrets_1
import ESMissionTechnologicalSecrets2 as technological_secrets_2
import ESMissionTechnologicalSecrets3 as technological_secrets_3

def inStation():
    x, y = image.findImgR(panel.Menu,
        'img/undock.bmp', 0.2)
    if x > 0 and y > 0:
        return True
    return False

bots = {'Gone Berserk':gone_berserk,
        'The Drug Bust':the_drug_bust,
        'Unauthorized Militarg Presence':unauthorized_military_presence,
        'Avenge a Fallen Comrade':avenge_a_fallen_comrade,
        'Customs lnterdictian (1 of 2)':customs_interdictian_1,
        'Customs lnterdictian (2 of 2)':customs_interdictian_2,
        'Deadlg Arrival':deadly_arrival,
        'Labors of War (1 of 3)':labors_of_war_1,
        'Labors of War (2 of 3)':labors_of_war_2,
        'Labors of War (3 of 3)':labors_of_war_3,
        'Pirate Intrusion':pirate_intrusion,
        'The Hidden Stash':the_hidden_stash,
        'Mission of Hem;':mission_of_mercy,
        'Renon (1 of 3)':recon_1,
        'Renon (2 of 3)':recon_2,
        'Renon (3 of 3)':recon_3,
        'The Damsel In Distress':the_damsel_in_distress, #v
        'The Sansha Spies':the_sansha_spies,
        'Tenhnalaginal Secrets (1 of 3)':technological_secrets_1,
        'Tenhnalaginal Secrets (2 of 3)':technological_secrets_2,
        'Tenhnalaginal Secrets (3 of 3)':technological_secrets_3,
        }

agent = 'img/agent.bmp'

def run():
    # if not inStation():
    #     print 'Error: Must begin at station.'
    #     return

    # print 'mission bot begin. \n'
    # while True:

    #     if not station.startConversation(agent):
    #         print 'Error: Could not find target agent.'
    #         return

    #     mission = image.extractTextR(panel.MissionName).strip()
    #     if mission not in bots:
    #         print 'Error: Cant find bot for mission \'' + mission + '\'.'
    #         return
    #     bot = bots[mission]

    #     print 'Mission - ' + mission
    #     if not station.acceptMission():
    #         print 'Error: Accept mission failed.'
    #         return

    #     if not space.setMissionWaypoint():
    #         print 'Error: Cant set mission waypoint.'
    #         return

        # TODO:test
        bot = bots['Tenhnalaginal Secrets (3 of 3)']

        # TODO:test
        mouse.moveTo(1000, 100)
        mouse.leftClick()

        if not bot.run():
            print 'Error: Mission abort.'
            return

        if not station.startConversation(agent):
            print 'Error: Could not find target agent.'
            return

        if not station.completeMission():
            print 'Error: Complete mission failed'
            return

        # if bot == bots['Tenhnalaginal Secrets (2 of 3)']:
        #     station.undock()
        #     pilot.autopilot()

        # TODO
        # break

if __name__ == '__main__':
    run()