#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import smach
import time
import smach_ros
from state.Start import Start
from state.RunStraight import RunStraight
from state.ChangeLine import ChangeLine
from state.Stop import Stop


class MainSM():
    def __init__(self):
        rospy.init_node('Smach_demo', anonymous=True)
        #rospy.on_shutdown(self.shutdown)

        """Create a smach state machine"""
        sm = smach.StateMachine(outcomes=['SUCCESSFUL', 'FAILED'])

        """Open the container"""
        with sm:
            """Add states to the container"""
            smach.StateMachine.add('START', Start(),
                                   transitions={'RunStraight': 'RUNSTRAIGHT',
                                                'ChangeLine': 'CHANGELINE'})
            smach.StateMachine.add('RUNSTRAIGHT', RunStraight(),
                                   transitions={'Stop': 'STOP'})
            smach.StateMachine.add('CHANGELINE', ChangeLine(),
                                   transitions={'Stop': 'STOP'})
            smach.StateMachine.add('STOP', Stop(),
                                   transitions={'Start': 'START'})

        """Create and start the introspection server"""
        sis = smach_ros.IntrospectionServer('start_state_machine', sm, '/SM_Trigger')
        sis.start()

        """Execute SMACH plan"""
        sm.execute()

        rospy.loginfo("Starting Smach test")
        #while not rospy.is_shutdown():
            #pass

        """Wait for ctrl-c to stop the application"""
        """In Python, if there is a while loop, the function spin() is redundant and useless"""
        rospy.spin()
        sis.stop()


if __name__ == '__main__':
    try:
        MainSM()
    except rospy.ROSInterruptException:
        rospy.loginfo("Smach Test Finished!")
