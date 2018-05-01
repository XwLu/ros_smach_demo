# -*- coding: UTF-8 -*-

import rospy
import smach
import time


class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Start'])

    def execute(self, userdata):
        rospy.loginfo('Stopped')
        time.sleep(2)
        rospy.loginfo('Going to Start')
        return 'Start'