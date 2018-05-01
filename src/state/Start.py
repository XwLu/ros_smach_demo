# -*- coding: UTF-8 -*-

import rospy
import smach
import time


class Start(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['RunStraight', 'ChangeLine'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Started!')
        time.sleep(2)
        rospy.loginfo('Going to Run Straightly')
        if self.counter < 2:
            self.counter += 1
            return 'RunStraight'
        else:
            self.counter = 0
            return 'ChangeLine'
