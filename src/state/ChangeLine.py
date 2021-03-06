# -*- coding: UTF-8 -*-

import rospy
import smach
import time


class ChangeLine(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Stop'])

    def execute(self, userdata):
        rospy.loginfo('Changing line')
        time.sleep(2)
        rospy.loginfo('Going to Stop')
        return 'Stop'