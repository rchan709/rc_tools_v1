import maya.cmds as cmds
import time
import sys
import json
import os
from pathlib import Path

# Call packages as modules

# Global varibles
script_path = sys.path[0][0:sys.path[0].rfind('/scripts')]+ '/prefs/scripts'

rc_toolWin = 'rc_toolsWin'
rc_height_field = 'height_field'
locator_prefix = 'loc_'
locator_suffix = '_loc'
joint_suffix = '_jnt'
control_suffix = '_ctrl'
group_suffix = '_grp'
do_not_export_prefix = 'DNE_'

RC_CREATED = list()

# Create the window
def rc_tool():
    #if the window is exsit, delete it
    if cmds.window(rc_toolWin, exists = 1):
        cmds.deleteUI(rc_toolWin, window = 1)
    
    # Run the function to create the window
    rc_toolUI()

    # initialize the window position and size
    cmds.windowPref(rc_toolWin, remove = True)
    cmds.window(rc_toolWin, edit = True,  topLeftCorner = (200, 200))
    #show the window
    cmds.showWindow(rc_toolWin)
    
def rc_toolUI():
    #initial the window
    ccWin = cmds.window(rc_toolWin, title = 'rc_tools v1.0', resizeToFitChildren = 1,  sizeable = 0)
    
    # The main layout: column
    mainLayout = cmds.columnLayout( adjustableColumn = 1, width = 300)
    
    # Layout of the units frame
    cmds.frameLayout(label = 'Units')
    cmds.columnLayout(columnAttach = ('left', 0))
    cmds.button(label = 'cm', w = 100, command = change_unit_cm)
    cmds.button(label = 'meter', w = 100, command = change_unit_m)
    cmds.button(label = 'inch', w = 100, command = change_unit_in)
    cmds.button(label = 'foot', w = 100, command = change_unit_ft)
    current_unit = cmds.currentUnit(query = True)
    cmds.floatFieldGrp(rc_height_field, numberOfFields = 1, label = f'Object Height ({current_unit}): ', value1 = 2.0 , precision = 2)
    cmds.setParent(mainLayout)

    # Layout of the rig setup frame
    cmds.frameLayout(label = 'Rig Presets')
    cmds.columnLayout(columnAttach = ('left', 0))
    cmds.button(label = 'Biped', w = 100, command = biped_setup)
    cmds.button(label = 'Vehicle', w = 100, command = vehicle_setup)
    cmds.button(label = 'Gun', w = 100, command = gun_setup)
    cmds.setParent(mainLayout)

    # Layout of the mirroring frame
    cmds.frameLayout(label = 'Edit')
    cmds.columnLayout(columnAttach = ('left', 0))
    cmds.button(label = 'Mirror +X', w = 100, command = test)
    cmds.button(label = 'Mirror -X', w = 100, command = test)
    
    #cmds.scrollLayout(childResizable = 1)
    #cmds.gridLayout(numberOfColumns = 7, cellWidthHeight = (40, 40), width = 100)

    cmds.setParent(mainLayout)

    # Layout of the export frame
    cmds.frameLayout(label = 'Create')
    cmds.columnLayout(columnAttach = ('left', 0))
    cmds.button(label = 'Create Rig', w = 100, command = rig_build)
    cmds.button(label = 'Export for Unreal', w = 100, command = test)
    
    #cmds.scrollLayout(childResizable = 1)
    #cmds.gridLayout(numberOfColumns = 7, cellWidthHeight = (40, 40), width = 100)

    #cmds.setParent(mainLayout)



def change_unit_cm(self):
    past_unit = cmds.currentUnit(query = True)
    set_height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    cmds.currentUnit( linear='cm')
    current_unit = cmds.currentUnit(query = True)

    convert_and_update_unit(past_unit, current_unit, set_height)

def change_unit_m(self):
    past_unit = cmds.currentUnit(query = True)
    set_height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    cmds.currentUnit( linear='m')
    current_unit = cmds.currentUnit(query = True)
    
    convert_and_update_unit(past_unit, current_unit, set_height)

def change_unit_in(self):
    past_unit = cmds.currentUnit(query = True)
    set_height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    cmds.currentUnit( linear='in')
    current_unit = cmds.currentUnit(query = True)
    
    convert_and_update_unit(past_unit, current_unit, set_height)

def change_unit_ft(self):
    past_unit = cmds.currentUnit(query = True)
    set_height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    cmds.currentUnit( linear='ft')
    current_unit = cmds.currentUnit(query = True)
    
    convert_and_update_unit(past_unit, current_unit, set_height)

def convert_and_update_unit(input_unit, output_unit, input_val):
    # convert everything to cm
    if input_unit == 'm':
        val = input_val * 100
    elif input_unit == 'in':
        val = input_val * 2.54
    elif input_unit == 'ft':
        val = input_val * 30.48
    else:
        val = input_val

    # calc cm to everything
    if output_unit == 'm':
        output_val = val / 100
    elif output_unit == 'in':
        output_val = val / 2.54
    elif output_unit == 'ft':
        output_val = val / 30.48
    else:
        output_val = val

    cmds.floatFieldGrp(rc_height_field, edit=True, label = f'Object Height ({output_unit}): ', value1 = output_val)

    #This resize grid to current units.
    mel.eval('GridOptions;')
    mel.eval('gridCallback OptionBoxWindow|formLayout141|tabLayout9|formLayout143|tabLayout10|columnLayout2011 1;')
    all_windows = cmds.lsUI( windows=True )
    for win in all_windows:
        if win == 'OptionBoxWindow':
            cmds.deleteUI(win)
            return


def test(self):
    print('pushed')


def height_obj_setup():
    height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    current_unit = cmds.currentUnit(query = True)
    cmds.select(cl = True)
    height_shape = import_ctrl_shape('circle_wide', name = f'height_{height}{current_unit}', loc = (0, height, 0), scale_shape = [height/4, height/4, height/4])[0]
    change_color_controls(height_shape, 28)
    l_attr = list()
    for a in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']:
        l_attr.append(f'{height_shape}.{a}')
    lock_attr(l_attr)

    #cmds.xform(height_shape, t = (0, height, 0), scale = (height/4, height/4, height/4))


    '''
    disk = mel.eval(f'polyDisc -sides 3 -subdivisionMode 4 -subdivisions 1 -radius {disk_radius};')
    #print(disk)
    disk = cmds.ls(disk, type = 'transform')[0]
    #print(disk)
    disk = poly_to_ctrl(disk, 'set_height_ctrl')
    #print(disk)
    cmds.select(disk)
    cmds.xform(t = (0, height, 0))
    '''
    return height_shape

# Error handeling???
'''
exc_type, exc_obj, exc_tb = sys.exc_info()
fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
print(exc_type, fname, exc_tb.tb_lineno)
'''
def biped_setup(self):
    ''' Sets up the biped's locators, then are moved by user. '''
    try:
        rig_preset = 'biped'
        main_group_name = f'{rig_preset}_rig'
        setup_group_name = f'{main_group_name}_setup_grp'

        if cmds.objExists(main_group_name):
            confirm = cmds.confirmDialog(title = 'Biped already exists!!', message = 'This will remove the current rig and start fresh.', button = ['Overwrite', 'Cancel'], cancelButton = 'Cancel')
            print(confirm)
            if confirm == 'Cancel':
                return
            else:
                to_delete(main_group_name)
                #cmds.delete(main_group_name)

        main_loc_group = cmds.group(name = main_group_name, empty = True)
        rig_setup_group = cmds.group(name = setup_group_name, empty=True)
            
        height_obj = height_obj_setup()
        cmds.parent(height_obj, setup_group_name)

        biped_locs = import_rig_setup(rig_preset)
        cmds.parent(biped_locs, rig_setup_group)
        
        cmds.parent(rig_setup_group, main_loc_group)

    except Exception as e:
        cmds.warning(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        

def vehicle_setup(self):
    print('vehicle')

def gun_setup(self):
    print('gun')






def rig_build(self):
    print('Creating Rig')

    
    height_scale_group = cmds.ls('*_height_scale_grp')[0]
    height_scale = cmds.getAttr(f'{height_scale_group}.scaleX')
    
    locator_group = cmds.ls(f'*_height_scale{group_suffix}')[0]
    main_loc_group = cmds.ls('*_rig')[0]

    rig_type = main_loc_group.replace('_rig', '')

    if not locator_group or not main_loc_group:
        print('There is no rig setup to build.')
        return

    joint_group = locator_to_joints(locator_group)
    joints = cmds.listRelatives(joint_group, allDescendents = True, type = 'joint')
    for j in joints:
        cmds.setAttr(f'{j}.segmentScaleCompensate', 0)
    cmds.parent(joint_group, main_loc_group)
        
    if rig_type == 'biped':

        controls_group = controls_for_biped(joints, height_scale)

    elif rig_type == 'vehicle':
        #controls_group = controls_for_vehicle(joints)
        pass

    elif rig_type == 'gun':
        #controls_group = controls_for_gun(joints)
        pass

    # Parent groups created in controls for _______ to main group
    '''
    for group in controls_group:
        cmds.parent(group, main_loc_group)
    '''


def controls_for_biped(joints, height_scale):
    main_loc_group = cmds.ls('*_rig')[0]
    setup_group = cmds.ls('*_setup_grp')[0]
    controls_group = cmds.group(name = 'controls' + group_suffix, empty=True)
    systems_group = cmds.group(name = 'DO_NOT_TOUCH', empty=True)
    constraints_group = cmds.group(name = 'constraints' + group_suffix, empty=True, parent = systems_group)
    systems_joints_group = cmds.group(name = 'DNE_joints' + group_suffix, empty=True, parent = systems_group)
    cmds.parent([controls_group, systems_group], main_loc_group)

    # Why cant get height scale be used here, but most importantly not in create_control_for_joint?
    #height_scale_group = cmds.ls('*_height_scale_grp')[0]
    #height_scale = cmds.getAttr(f'{height_scale_group}.scaleX')


    try:

        root_control = create_control_for_joint(f'root{joint_suffix}', shape = 'pentagon', rot_shape = [0,0,0], scale = [2,2,2])
        cmds.parent(root_control[0][0], controls_group)
        pelvis_control = create_control_for_joint(f'pelvis{joint_suffix}', parent = root_control[1], shape = 'ring', rot_shape = [0,0,86.367], scale = [1,.3,1]) 
            
        
        #spine_01 - spine_05
        spine_list = list()
        for i, spine in enumerate(cmds.ls(f'spine_*{joint_suffix}')):
            if i == 0:
                spine_list.append(create_control_for_joint(spine, parent = pelvis_control[1], shape = 'bean_thin', loc_shape = [0,.12,0], scale = [.1,.1,.1]))
            else:
                spine_list.append(create_control_for_joint(spine, parent = spine_list[-1][1], shape = 'bean_thin', loc_shape = [0,.12,0], scale = [.1,.1,.1]))
         
        #neck_01 - neck_02
        neck_list = list()
        for i, neck in enumerate(cmds.ls(f'neck_*{joint_suffix}')):
            if i == 0:
                neck_list.append(create_control_for_joint(neck, parent = spine_list[-1][1], scale = [.1,.1,.1]))
            else:
                neck_list.append(create_control_for_joint(neck, parent = neck_list[-1][1], scale = [.1,.1,.1]))
        
        
        #head
        head_joint = f'head{joint_suffix}'
        if len(cmds.ls(head_joint)) > 0:
            head_control = create_control_for_joint(f'head{joint_suffix}', parent = neck_list[-1][1], shape = 'cube', loc_shape = [.06,-.03,0], scale = [.14,.13,.1])
        else:
            print('Head Joint wasnt found.')
        #ik_foot_root
        ik_foot_root = create_control_for_joint(f'ik_foot_root{joint_suffix}', parent = root_control[1], shape = 'tetrahedron', rot_shape = [90,0,-90], scale = [.1,.1,.1])

        #ik_hand_root
        ik_hand_root = create_control_for_joint(f'ik_hand_root{joint_suffix}', parent = root_control[1], shape = 'tetrahedron', loc_shape = [0.1,0,0], rot_shape = [90,0,-90], scale = [.1,.1,.1])

        #interaction
        interaction = create_control_for_joint(f'interaction{joint_suffix}', parent = root_control[1], shape = 'gear', loc_shape = [0,-.5,0], rot_shape = [90,0,0], scale = [.2,.2,.2])

        #center_of_mass
        center_of_mass = create_control_for_joint(f'center_of_mass{joint_suffix}', parent = root_control[1], shape = 'circle_wave', rot_shape = [90,0,0])

        l_clavical = create_control_for_joint(f'clavicle_l{joint_suffix}', parent = spine_list[-1][1], shape = 'bean', loc_shape = [.03,.2,0], scale = [.1,.05,.1]) 
        #l_arm_ik_switch_control = create_control_for_joint(l_clavical[1][0], name = 'l_arm_ik_switch', parent = l_clavical[0][0], shape = 'gear', loc_shape = [.06,.2,0], scale = [0.05,0.05,0.05], constrain = False)
        r_clavical = create_control_for_joint(f'clavicle_r{joint_suffix}', parent = spine_list[-1][1], shape = 'bean', loc_shape = [-.03,-.2,0], rot_shape = [180,0,0], scale = [.1,.05,.1])
        #r_arm_ik_switch_control = create_control_for_joint(r_clavical[1][0], name = 'r_arm_ik_switch', parent = r_clavical[0][0], shape = 'gear', loc_shape = [-.06,-.2,0], scale = [0.05,0.05,0.05], constrain = False)

        # Change switch to top spine
        arm_ik_switch_control = create_control_for_joint(spine_list[-1][1], name = 'arm_ik_switch', parent = spine_list[-1][1], shape = 'gear', loc_shape = [0,.25,0], scale = [0.08,0.08,0.08], constrain = False)
        leg_ik_switch_control = create_control_for_joint(spine_list[0][1], name = 'leg_ik_switch', parent = spine_list[0][1], shape = 'gear', loc_shape = [0,.25,0], scale = [0.08,0.08,0.08], constrain = False)

        #Fingers
        l_fingers_list = list()
        r_fingers_list = list()
        fingers_list = list()
        for side in ['l', 'r']:
            hand_joint = cmds.ls(f'hand_{side}{joint_suffix}')[0]
            finger_base = cmds.listRelatives(hand_joint)

            # Create Group for controls to go in
            hand_grp = cmds.group(name = f'hand_{side}{group_suffix}', parent = hand_joint, empty = True)
            cmds.parent(hand_grp, root_control[1])
            thing = cmds.parentConstraint(hand_joint, hand_grp, maintainOffset = True)
            cmds.parent(thing, constraints_group)

            for finger in finger_base:
                if side == 'l':
                    fingers_list.append(create_control_for_joint(finger, parent = hand_grp, shape = 'pyramid_45', loc_shape = [0,-.02,0], rot_shape = [180,0,0], scale = [.02,.02,.02]))
                elif side == 'r':
                    fingers_list.append(create_control_for_joint(finger, parent = hand_grp, shape = 'pyramid_45', loc_shape = [0,.02,0], scale = [.02,.02,.02]))

                # Constraining the metacarples to the hand joint
                finger_constraint = cmds.parentConstraint(hand_joint, fingers_list[-1][0], mo = True)
                cmds.parent(finger_constraint, constraints_group)

                digits = cmds.listRelatives(finger, allDescendents = True)
                digits.sort()
                for i, digit in enumerate(digits):
                    if side == 'l':
                        fingers_list.append(create_control_for_joint(digit, parent = fingers_list[-1][1], shape = 'pyramid_45', loc_shape = [0,-.02,0], rot_shape = [180,0,0], scale = [.01,.01,.01]))
                    elif side == 'r':
                        fingers_list.append(create_control_for_joint(digit, parent = fingers_list[-1][1], shape = 'pyramid_45', loc_shape = [0,.02,0], scale = [.01,.01,.01]))


        '''
        DEPRICATED Combined these loops

        #L_fingers
        l_fingers_list = list()
        hand_joint = cmds.ls(f'hand_l{joint_suffix}')[0]
        l_finger_base = cmds.listRelatives(hand_joint)
        for finger in l_finger_base:
            l_fingers_list.append(create_control_for_joint(finger, height_scale, parent = root_control[1], shape = 'pyramid_45', loc_shape = [0,-.02,0], rot_shape = [180,0,0], scale = [.02,.02,.02]))
            finger_constraint = cmds.parentConstraint(hand_joint, l_fingers_list[-1][0], mo = True)
            cmds.parent(finger_constraint, constraints_group)
            digits = cmds.listRelatives(finger, allDescendents = True)
            digits.sort()
            for i, digit in enumerate(digits):
                print(cmds.listRelatives(finger, allDescendents = True))
                l_fingers_list.append(create_control_for_joint(digit, height_scale, parent = l_fingers_list[-1][1], shape = 'pyramid_45', loc_shape = [0,-.02,0], rot_shape = [180,0,0], scale = [.01,.01,.01]))

        #R_fingers
        r_fingers_list = list()
        hand_joint = cmds.ls(f'hand_r{joint_suffix}')[0]
        r_finger_base = cmds.listRelatives(hand_joint)
        for finger in r_finger_base:
            r_fingers_list.append(create_control_for_joint(finger, height_scale, parent = root_control[1], shape = 'pyramid_45', loc_shape = [0,.02,0], scale = [.02,.02,.02]))
            finger_constraint = cmds.parentConstraint(hand_joint, r_fingers_list[-1][0], mo = True)
            cmds.parent(finger_constraint, constraints_group)
            digits = cmds.listRelatives(finger, allDescendents = True)
            digits.sort()
            for i, digit in enumerate(digits):
                print(cmds.listRelatives(finger, allDescendents = True))
                r_fingers_list.append(create_control_for_joint(digit, height_scale, parent = r_fingers_list[-1][1], shape = 'pyramid_45', loc_shape = [0,.02,0], scale = [.01,.01,.01]))
        '''
        

        print('FINISHED UP TO FINGERS\n\n\n\n')

        
            
        for side in ['r', 'l']:
            #arm_controls = arm_setup(f'upperarm_{side}{joint_suffix}', f'lowerarm_{side}{joint_suffix}', f'hand_{side}{joint_suffix}', root = root_control[1], ik_jnt = f'ik_foot_{side}{joint_suffix}', side = side)
            '''
            if side == 'l':
                arm_switch = l_arm_ik_switch_control[1][0]
            else:
                arm_switch = r_arm_ik_switch_control[1][0]
            '''

            arm_controls = arm_setup(f'upperarm_{side}{joint_suffix}', f'lowerarm_{side}{joint_suffix}', f'hand_{side}{joint_suffix}', ik_jnt = f'ik_hand_{side}{joint_suffix}', side = side, switch = arm_ik_switch_control[1][0])

            leg_controls = leg_setup(f'thigh_{side}{joint_suffix}', f'calf_{side}{joint_suffix}', f'foot_{side}{joint_suffix}', f'ball_{side}{joint_suffix}', root = root_control[1], ik_jnt = f'ik_foot_{side}{joint_suffix}', side = side)
            
        

        #no left and right side loop because of ctrl shape
        # Coloring Controls
        left_controls = cmds.ls(f'*_l{control_suffix}')
        for ctrl in left_controls:
            cmds.setAttr(f'{ctrl}.overrideEnabled', 1)
            cmds.setAttr(f'{ctrl}.overrideColor', 6)

        right_controls = cmds.ls(f'*_r{control_suffix}')
        for ctrl in right_controls:
            cmds.setAttr(f'{ctrl}.overrideEnabled', 1)
            cmds.setAttr(f'{ctrl}.overrideColor', 13)


        return
    
        for side in ['r', 'l']:

            # IK FK leg Setup
            #leg_setup = leg_setup(f'thigh_{side}{joint_suffix}', f'calf_{side}{joint_suffix}', f'foot_{side}{joint_suffix}', f'ball_{side}{joint_suffix}', root_control[1], ik_jnt = f'ik_foot_{side}{joint_suffix}')
            #cmds.parent(leg_setup, pelvis_control)

            # Clavical
            clavical = create_control_for_joint(f'clavicle_{side}{joint_suffix}', height_scale, parent = spine_list[-1][1], shape = 'bean') 
            continue
            # IK FK arm Setup
            ik_arm_setup = arm_setup(f'upperarm_{side}{joint_suffix}', f'lowerarm_{side}{joint_suffix}', f'hand_{side}{joint_suffix}', root_control[1], ik_jnt = f'ik_hand_{side}{joint_suffix}')
            cmds.parent(ik_arm_setup, clavical)
            
            # Finger Controls
            for finger in ['thumb', 'index', 'middle', 'ring', 'pinky']:
                first_digit_joint = f'{finger}_metacarpal_{side}{joint_suffix}'

                #parents first digit to the hand joint           
                first_digit = create_control_for_joint(first_digit_joint, f'hand_{side}{joint_suffix}')

                # Has to be the correct order so the parent exists when creating the children. .reverse() doesnt seem to work?
                #finger_digits = cmds.listRelatives(first_digit_joint, allDescendents = True, type = 'joint').reverse()
                '''
                finger_digits = cmds.listRelatives(first_digit_joint, allDescendents = True, type = 'joint')
                finger_list = list()
                for i in range(len(finger_digits)):
                    
                    if i == 0:
                        finger_list.append(create_control_for_joint(finger_digits.pop(), first_digit[1]))
                    else:
                        finger_list.append(create_control_for_joint(finger_digits.pop(), finger_list[-1][1]))

                thursday 4pm office depot
                '''

                finger_list = list()
                finger_joint = cmds.ls(f'{finger}_*_{side}{joint_suffix}')
                for i, digit in enumerate(finger_joint):
                    if i == 0:
                        finger_list.append(create_control_for_joint(digit, first_digit[1]))
                    else:
                        finger_list.append(create_control_for_joint(digit, finger_list[-1][1]))
    
        #auto_color_controls(controls_group)
        #change_color_controls(ik_switcher_ctrl, 16)
                        
        # Stores perfered joint angle or root (I think you only need the root)
        #joint -e -spa -ch root_jnt;
                        
        # Move joints to a joint layer
        # move Controls to a control layer
        # create a geo layer
        # have some sort of dialoge to get the namespace
        # space switching between locations (like changing the ik hand)
                    
    except Exception as e:
        cmds.warning(f'     ##### Error: {e} #####')
        cmds.warning('Controls deleted...')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return
        cmds.delete(controls_group, systems_group)
    finally:
        # Maybe at the end of the try instead
        print('Finally delete setup group.')
        #cmds.delete(setup_group)

    return controls_group, systems_group


def get_height_scale():
    height_scale_group = cmds.ls('*_height_scale_grp')[0]
    height_scale = cmds.getAttr(f'{height_scale_group}.scaleX')
    return height_scale

def create_control_for_joint(joint, name = None, parent = None, shape = 'circle', loc_shape = [0,0,0], rot_shape = [0,0,0], scale = [1,1,1], shape_flip = False, constrain = True):
    '''
    arguments:
        joint: The joint that is going to be driven by this control and also position
        height_scale (float): this is what the locs are scaled to to achieve the desired height (could be a global value)
        parent: Where the control_group is going to be parented to
        shape: The shape of the control curve
        loc, rot: The transforms that the shape is relative to the joint
    return:
        The control group and the control shape so that the group can be parented and other controls can be parented to.
    '''
    systems_group = cmds.ls('DO_NOT_TOUCH')[0]
    constraints_group = cmds.ls('constraints' + group_suffix)[0]
    print(f'Creating control for {joint}')
    name = name or joint.replace(joint_suffix, '')

    '''
    height_scale_group = cmds.ls('*_height_scale_grp')[0]
    height_scale = cmds.getAttr(f'{height_scale_group}.scaleX')
    '''
    height_scale = get_height_scale()

    #Maybe scale loc_shape, rot_shape, and scale to the scale of biped_height_scale_grp
    for i in range(3):
        loc_shape[i] = loc_shape[i] * height_scale
        scale[i] = scale[i] * height_scale

    '''
    loc_shape = [loc_shape[i] * height_scale for i in range(3)]
    rot_shape = [rot_shape[i] * height_scale for i in range(3)]
    scale = [scale[i] * height_scale for i in range(3)]
    '''

    if shape_flip:
        scale = [scale[i] * height_scale for i in range(3)]

    #control_group = cmds.group(name = name + group_suffix, empty=True)
    #location = cmds.xform(joint, query = True, translation = True, worldSpace = True)
    #rotation = cmds.xform(joint, query = True, rotation = True, worldSpace = True)
    #control_group, control_shape = import_ctrl_shape(shape, name = name, num_of_group = 1, add_suffix = True, loc = location, rot = rotation, loc_shape = loc_shape, rot_shape = rot_shape, scale = scale)
    cmds.select(joint)  # import_ctrl_shape takes a selected object and matches location and rotation
    control_group, control_shape = import_ctrl_shape(shape, name = name, num_of_group = 1, add_suffix = True, loc_shape = loc_shape, rot_shape = rot_shape, scale_shape = scale)
    #control_shape = cmds.rename(control_shape, name + control_suffix)
    
    # Transform the curve shape, but some have multiple shapes
    #cmds.xform()
    cmds.matchTransform(control_group, joint)

    if parent:
        cmds.parent(control_group, parent)

    #cmds.matchTransform(control_group, joint)
    if constrain:
        # Constrain added to make a blank control that doesnt drive anything yet... (The ik hand for example)
        parent_constraint = cmds.parentConstraint(control_shape, joint, maintainOffset = True)
        cmds.parent(parent_constraint, constraints_group)

    print(f'Finished control for {joint}')

    return control_group, control_shape

def arm_setup(upperarm, lowerarm, hand, root = None, ik_jnt = None, side = None, switch = None):
    '''
    (bind_joint_top, bind_joint_mid, bind_joint_bottom, switch_control, pole_vector_parent = None, top_joint_parent = None, attr_name = 'IKFK_Switch'):
    arguments:
        upperarm: the joint that is at the top of the chain that is exported.
        lowerarm: the joint that is at the middle of the chain that is exported.
        hand: the joint that is at the bottom of the chain that is exported.
        root: where the pole vector control is parented. (give the root ctrl usually)
        ik: the joint that drives the ik?
        side: adding prefixes to controls

    return:
        maybe return base_group and end?
    '''

    arm_parent = cmds.listRelatives(upperarm, parent = True)
    switch_control = switch or cmds.ls(f'interaction{control_suffix}')[0]

    if side:
        attr_name = f'arm_{side}_IKFK'
    else:
        attr_name = 'arm_IKFK'
    create_2_jnt_ik_setup(upperarm, lowerarm, hand, switch_control, pole_vector_parent = root, top_joint_parent = arm_parent, attr_name = attr_name)

    #find twist joints then create controls
    for joint in [upperarm, lowerarm]:
        decendants = cmds.listRelatives(joint)
        twist_joints = list()
        for things in decendants:
            if things.find('twist') > 0:
                twist_joints.append(things)
        if twist_joints:
            print('Theres existing twist joints in upperarm')
            #create controls
        else:
            if joint == upperarm:
                create_twist_joints(upperarm, lowerarm, 2)
            elif joint == lowerarm:
                create_twist_joints(lowerarm, hand, 2)
    
    return
    

def leg_setup(thigh, calf, foot, ball, root = None, ik_jnt = None, side = None):
    '''
    arguments:
        thigh: the joint that is at the top of the chain that is exported.
        calf: the joint that is at the middle of the chain that is exported.
        foot: the joint that is at the bottom of the chain that is exported.
        ball: the control that will have the ik/fk switch added to.
        root: where the pole vector control is parented. (give the root ctrl usually)
        ik_jnt: the joint in the rig that drives the ik?
        side: adding prefixes to controls

    return:
        maybe return base_group and end?
    '''
    leg_parent = cmds.listRelatives(thigh, parent = True)
    switch_control = cmds.ls(f'interaction{control_suffix}')[0]

    if side:
        attr_name = f'leg_{side}_IKFK'
    else:
        attr_name = 'leg_IKFK'

    leg = create_2_jnt_ik_setup(thigh, calf, foot, switch_control, pole_vector_parent = root, top_joint_parent = leg_parent, attr_name = attr_name)
    ik_joint_root = leg[0][0][-1]
    ik_control_root = leg[0][1][-1]
    fk_joint_root = leg[1][0][-1]
    fk_control_root = leg[1][1][-1]

    create_1_jnt_ik_setup(foot, ball, switch_control, attr_name = attr_name, ik_joint_root = ik_joint_root, ik_control_root = ik_control_root, fk_joint_root = fk_joint_root, fk_control_root = fk_control_root)

    #find twist joints then create controls
    for joint in [thigh, calf]:
        decendants = cmds.listRelatives(joint)
        twist_joints = list()
        for things in decendants:
            if things.find('twist') > 0:
                twist_joints.append(things)
        if twist_joints:
            print('Theres existing twist joints in thigh')
            #create controls
        else:
            if joint == thigh:
                create_twist_joints(thigh, calf, 2)
            elif joint == calf:
                create_twist_joints(calf, foot, 2)
    
    #Create ball control with roll
    return 

def to_delete(*args):
    '''
    arguments: Anything to be deleted.
    '''
    for item in args:
        if not item:
            continue
        cmds.select(item)
        cmds.delete()


def create_1_jnt_ik_setup(bind_joint_top, bind_joint_bottom, switch_control, attr_name = 'IKFK_Switch', ik_joint_root = None, ik_control_root = None, fk_joint_root = None, fk_control_root = None):
    '''
    arguments:
        bind_joint_top: the joint that is at the top of the chain that is exported.
        bind_joint_bottom: the joint that is at the bottom of the chain that is exported.
        switch_control: the control that will have the ik/fk switch added to.
        pole_vector_parent: where the pole vector control is parented. (give the root ctrl usually)
        top_joint_parent: the joint the new joints are going to be parented to.
        control_name: 

    return:
    '''
    print('create_1_jnt_ik_setup')
    # instead of switch control have f'{switch_control}.{attr_name}' as the input, create attribute if it doesnt exist yet.

    ik_joints = list()
    ik_controls = list()
    fk_joints = list()
    fk_controls = list()
    joint_list = [bind_joint_top, bind_joint_bottom]

    systems_group = cmds.ls('DO_NOT_TOUCH')[0]
    constraints_group = cmds.ls('constraints' + group_suffix)[0]
    systems_joints_group = cmds.ls(f'DNE_joints{group_suffix}')[0]

    top_joint_name = bind_joint_top[:(len(bind_joint_top) - len(joint_suffix))]
    bottom_joint_name = bind_joint_bottom[:(len(bind_joint_bottom) - len(joint_suffix))]
  
    joint_top_parent = cmds.listRelatives(bind_joint_top, parent = True)[0]
    control_top_parent = joint_top_parent.replace(joint_suffix, control_suffix)

    try:

        #Adds Attribute to switch
        if not cmds.attributeQuery(f'{switch_control}.{attr_name}', exists = True):
            print('Attribute Created')
            cmds.addAttr(switch_control, longName = attr_name, attributeType = 'double', min = 0, max = 1, keyable = True)

        # Creating the ik and fk joint chains
        for ikfk in ['ik', 'fk']:
            for joint in joint_list:
                # Making the joints
                new_joint_parent = f'{do_not_export_prefix}{ikfk}_{cmds.listRelatives(joint, parent = True)[0]}'
                new_joint = cmds.joint(None, name = f'{do_not_export_prefix}{ikfk}_{joint}')
                cmds.matchTransform(new_joint, joint)
                
                # Parent constraint the new chain base to target root joint
                if joint != bind_joint_top:
                    cmds.parent(new_joint, new_joint_parent)

                if ikfk == 'ik':
                    ik_joints.append(new_joint)
                else:
                    fk_joints.append(new_joint)

        # Move joints to parents
        cmds.parent(ik_joints[0], ik_joint_root or systems_joints_group)
        cmds.parent(fk_joints[0], fk_joint_root or systems_joints_group)

        '''
        if ik_joint_root:
            cmds.parent(ik_joints[0], ik_joint_root)
        else:
            cmds.parent(ik_joints[0], systems_joints_group)
        
        if fk_joint_root:
            cmds.parent(fk_joints[0], fk_joint_root)
        else:
            cmds.parent(fk_joints[0], systems_joints_group)
        '''

        # Parent constraint joints to drive the bind joints
        for i, joint in enumerate(joint_list):
            ikfk_constraint = cmds.orientConstraint(fk_joints[i], ik_joints[i], joint, maintainOffset = True)[0]
            cmds.parent(ikfk_constraint, systems_group)
            targetList = cmds.orientConstraint(ikfk_constraint, query=True, targetList=True)
            attrs = cmds.listAttr(ikfk_constraint, keyable = True)
            ik_target_attr = ''
            fk_target_attr = ''
            for attr in attrs:
                for target in targetList:
                    if target in attr:
                        if 'ik' in attr:
                            ik_target_attr = f'{ikfk_constraint}.{attr}'
                        elif 'fk' in attr:
                            fk_target_attr = f'{ikfk_constraint}.{attr}'

            #IK on, FK off
            cmds.setDrivenKeyframe(ik_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 0)
            cmds.setDrivenKeyframe(fk_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 1)

            #Ik off, FK on
            cmds.setDrivenKeyframe(ik_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 1)
            cmds.setDrivenKeyframe(fk_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 0)

        # Creating controls for fk controls
        for fk_joint in fk_joints:
            if fk_joint == fk_joints[0]:
                fk_joint_parent = fk_control_root
            else:
                fk_joint_parent = cmds.listRelatives(fk_joint, parent = True)[0]

            fk_control = create_control_for_joint(fk_joint, parent = fk_joint_parent, shape = 'circle', scale = [.1,.1,.1])[1]
            fk_controls.append(fk_control)
            cmds.setDrivenKeyframe(f'{fk_control[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 1)
            cmds.setDrivenKeyframe(f'{fk_control[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 0)

        # Parent the shoulder fk to the clavical
        top_ctrl_grp = cmds.listRelatives(fk_controls[0], parent = True)[0]
        cmds.parent(top_ctrl_grp, control_top_parent)


        ############################
        # Creating controls for ik #
        ############################

        # Setting preference angle fixes IK joint flipping
        cmds.joint(ik_joints[0], edit = True, children = True, setPreferredAngles = True)

        # IK Shoulder
        # Shoulder control might not be needed
        ik_shoulder_ctrl = create_control_for_joint(ik_joints[0], parent = control_top_parent, shape = 'handle_square', loc_shape = [0, 0, -0.1], rot_shape= [0, 0, 90], scale = [0.2, 0.2, 0.2])[1]
        ik_controls.append(ik_shoulder_ctrl)
        
        # Creating the IK handle
        # Control created at the bottom joint vefore any ik is made is to prevent issues if ik breaks, but maybe its good to see things break so i can fix it.
        ik_handle_ctrl = create_control_for_joint(bind_joint_bottom, parent = ik_control_root or f'root{control_suffix}', shape = 'circle', rot_shape= [0, 0, 0], scale = [0.08, 0.08, 0.08], constrain = False)
        ik_handle = cmds.ikHandle(name = f'{bottom_joint_name}_ik_handle', startJoint = ik_joints[0], endEffector = ik_joints[2], solver = 'ikSCsolver') # [ikHandle, effector]
        '''
        # mo = False gets us the correct result, but I think there are other issues in the joint rotations
        bottom_orient_constraint = cmds.orientConstraint(ik_handle_ctrl[1], ik_joints[2], mo = True)
        cmds.parent(bottom_orient_constraint, systems_group)
        cmds.parent(ik_handle[0], ik_handle_ctrl[1])
        ik_controls.append(ik_handle_ctrl[1])

        #Set visibility of IK controls
        for ik_ctrl in ik_controls:
            cmds.setDrivenKeyframe(f'{ik_ctrl[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 1)
            cmds.setDrivenKeyframe(f'{ik_ctrl[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 0)

        print(f'Finished create_1_jnt_ik_setup: {bind_joint_top}')

        return [ik_joints, ik_controls], [fk_joints, fk_controls]
        '''
    except Exception as e:
        cmds.warning(f'     ##### Error: {e} #####')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)



def create_2_jnt_ik_setup(bind_joint_top, bind_joint_mid, bind_joint_bottom, switch_control, pole_vector_parent = None, top_joint_parent = None, attr_name = 'IKFK_Switch'):
    '''
    arguments:
        bind_joint_top: the joint that is at the top of the chain that is exported.
        bind_joint_mid: the joint that is at the middle of the chain that is exported.
        bind_joint_bottom: the joint that is at the bottom of the chain that is exported.
        switch_control: the control that will have the ik/fk switch added to.
        pole_vector_parent: where the pole vector control is parented. (give the root ctrl usually)
        top_joint_parent: the joint the new joints are going to be parented to.
        control_name: 

    return:
        [[ik_joints], [ik_controls]],
        [fk_joints], [fk_controls]]
        maybe return the switch attribute so that the foot can be added?
    '''

    #returns groups, not controls (or maybe attachment points)
    #create ik and fk joints, parent constraint to parent of bind_joint_top

    ik_joints = list()
    ik_controls = list()
    fk_joints = list()
    fk_controls = list()
    joint_list = [bind_joint_top, bind_joint_mid, bind_joint_bottom]

    systems_group = cmds.ls('DO_NOT_TOUCH')[0]
    constraints_group = cmds.ls('constraints' + group_suffix)[0]
    systems_joints_group = cmds.ls(f'DNE_joints{group_suffix}')[0]

    top_joint_name = bind_joint_top[:(len(bind_joint_top) - len(joint_suffix))]
    mid_joint_name = bind_joint_mid[:(len(bind_joint_mid) - len(joint_suffix))]
    bottom_joint_name = bind_joint_bottom[:(len(bind_joint_bottom) - len(joint_suffix))]

    # Create group in systems_grp to have pole vector objects
    ik_setup_sys_group = cmds.group(name = f'ikfk_objects_{top_joint_name}{group_suffix}', parent = systems_group, empty = True)
    '''
    # I dont think there would be a situation were there wouldnt already be an IK systems group
    if cmds.ls(f'{top_joint_name}_ikfk_objects_{group_suffix}'):
        ik_setup_group = cmds.ls(f'{top_joint_name}_ikfk_objects_{group_suffix}')[0]
    else:
        ik_setup_group = cmds.group(name = f'{top_joint_name}_ikfk_objects_{group_suffix}', parent = systems_group, empty = True)
    '''

    joint_top_parent = cmds.listRelatives(bind_joint_top, parent = True)[0]
    control_top_parent = joint_top_parent.replace(joint_suffix, control_suffix)

    #Adds Attribute to switch
    cmds.addAttr(switch_control, longName = attr_name, attributeType = 'double', min = 0, max = 1, keyable = True)

    try:

        # Creating the ik and fk joint chains
        for ikfk in ['ik', 'fk']:
            for joint in joint_list:
                # Making the joints
                new_joint_parent = f'{do_not_export_prefix}{ikfk}_{cmds.listRelatives(joint, parent = True)[0]}'
                new_joint = cmds.joint(None, name = f'{do_not_export_prefix}{ikfk}_{joint}')
                cmds.matchTransform(new_joint, joint)
                
                # Parent constraint the new chain base to target root joint

                if joint != bind_joint_top:
                    cmds.parent(new_joint, new_joint_parent)

                '''
                the joint == bind joint might not be needed
                if joint == bind_joint_top:
                    # this is for parent constraining the top of the new joint chain to the parent of the bind_joint_top (clavical or hips).
                    #new_joint_root_parent_constraint = cmds.parentConstraint(cmds.listRelatives(bind_joint_top, parent = True)[0], new_joint, maintainOffset = True)
                    # move the parent constraint to the systems_group
                    print('no parent constraint from new top joint to clavical')
                else:
                    # Connect the new joints to the parent joint
                    cmds.parent(new_joint, new_joint_parent)
                '''
                if ikfk == 'ik':
                    ik_joints.append(new_joint)
                else:
                    fk_joints.append(new_joint)

        # Move joints to systems group
        cmds.parent(ik_joints[0], systems_joints_group)
        cmds.parent(fk_joints[0], systems_joints_group)
        
        # Parent constraint joints to drive the bind joints
        for i, joint in enumerate(joint_list):
            ikfk_constraint = cmds.orientConstraint(fk_joints[i], ik_joints[i], joint, maintainOffset = True)[0]
            cmds.parent(ikfk_constraint, ik_setup_sys_group)
            targetList = cmds.orientConstraint(ikfk_constraint, query=True, targetList=True)
            attrs = cmds.listAttr(ikfk_constraint, keyable = True)
            ik_target_attr = ''
            fk_target_attr = ''
            for attr in attrs:
                for target in targetList:
                    if target in attr:
                        if 'ik' in attr:
                            ik_target_attr = f'{ikfk_constraint}.{attr}'
                        elif 'fk' in attr:
                            fk_target_attr = f'{ikfk_constraint}.{attr}'

            #IK on, FK off
            cmds.setDrivenKeyframe(ik_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 0)
            cmds.setDrivenKeyframe(fk_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 1)

            #Ik off, FK on
            cmds.setDrivenKeyframe(ik_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 1)
            cmds.setDrivenKeyframe(fk_target_attr, currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 0)

        # Creating controls for fk controls
        for fk_joint in fk_joints:
            fk_joint_parent = cmds.listRelatives(fk_joint, parent = True) or cmds.parentConstraint(fk_joint, q=True, tl=True)
            fk_joint_parent = fk_joint_parent[0]
            print(f'Joint: {fk_joint}, parent: {fk_joint_parent}, listRelatives: {cmds.listRelatives(fk_joint, parent = True)}, parent const target list: {cmds.parentConstraint(fk_joint, q=True, tl=True)}')
            fk_control = create_control_for_joint(fk_joint, parent = fk_joint_parent, shape = 'circle', scale = [.1,.1,.1])[1]
            fk_controls.append(fk_control)

            cmds.setDrivenKeyframe(f'{fk_control[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 1)
            cmds.setDrivenKeyframe(f'{fk_control[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 0)

        # Parent the shoulder fk to the clavical
        top_ctrl_grp = cmds.listRelatives(fk_controls[0], parent = True)[0]
        cmds.parent(top_ctrl_grp, control_top_parent)

        #####################################
        # Creating controls for ik controls #
        #####################################

        # Setting preference angle fixes IK joint flipping
        cmds.joint(ik_joints[0], edit = True, children = True, setPreferredAngles = True)

        # IK Shoulder
        # Shoulder control might not be needed
        ik_shoulder_ctrl = create_control_for_joint(ik_joints[0], parent = control_top_parent, shape = 'handle_square', loc_shape = [0, 0, -0.1], rot_shape= [0, 0, 90], scale = [0.2, 0.2, 0.2])[1]
        ik_controls.append(ik_shoulder_ctrl)
        
        # Creating the IK handle
        # Control created at the bottom joint vefore any ik is made is to prevent issues if ik breaks, but maybe its good to see things break so i can fix it.
        ik_handle_ctrl = create_control_for_joint(bind_joint_bottom, parent = f'root{control_suffix}', shape = 'circle', rot_shape= [0, 0, 0], scale = [0.08, 0.08, 0.08], constrain = False)
        ik_handle = cmds.ikHandle(name = f'{bottom_joint_name}_ik_handle', startJoint = ik_joints[0], endEffector = ik_joints[2], solver = 'ikRPsolver') # [ikHandle, effector]
        #ik_handle_ctrl = create_control_for_joint(ik_handle[0], parent = f'root{control_suffix}', shape = 'circle', rot_shape= [0, 90, 0], scale = [0.08, 0.08, 0.08])

        
        # mo = False gets us the correct result, but I think there are other issues in the joint rotations
        bottom_orient_constraint = cmds.orientConstraint(ik_handle_ctrl[1], ik_joints[2], mo = True)
        cmds.parent(bottom_orient_constraint, ik_setup_sys_group)
        cmds.parent(ik_handle[0], ik_handle_ctrl[1])
        ik_controls.append(ik_handle_ctrl[1])
        
        # IK Pole Vector
        # Create polygon to find pole_vector_control location
        points = list()
        for joint in joint_list:
            #making a list of joint locations
            temp_locator = cmds.spaceLocator()
            cmds.matchTransform(temp_locator, joint)
            points.append(cmds.xform(temp_locator, query = True, absolute = True, translation = True))
            to_delete(temp_locator)
            #cmds.delete(temp_locator)

        # Creating temp poly plane
        temp_poly = cmds.polyCreateFacet(name = 'temp_plane', p = points)[0]

        # For some reason, when creating temp_poly, the points are scaled to cm instead of m? So moving points to joints
        for i in range(3):
            cmds.move(points[i][0], points[i][1], points[i][2], f'{temp_poly}.vtx[{i}]')

        # Move middle vertex out along plane.
        # Getting character height to move plane a quarter length away from mid joint
        poly_move_direction = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True) / 4

        # Check to see what direction the vertex needs to go by calculating the larger area after moving.
        positive_dupe = cmds.duplicate(temp_poly)[0]
        cmds.moveVertexAlongDirection(f'{positive_dupe}.vtx[1]', vDirection = poly_move_direction)
        positive_area = cmds.polyEvaluate(positive_dupe, area = True)
        to_delete(positive_dupe)

        negative_dupe = cmds.duplicate(temp_poly)[0]
        cmds.moveVertexAlongDirection(f'{negative_dupe}.vtx[1]', vDirection = -poly_move_direction)
        negative_area = cmds.polyEvaluate(negative_dupe, area = True)
        to_delete(negative_dupe)

        if negative_area > positive_area:
            poly_move_direction = -poly_move_direction

        # Move Poly out
        cmds.moveVertexAlongDirection(f'{temp_poly}.vtx[1]', vDirection = poly_move_direction)

        # Store vertex location then delete polygon.
        pole_vector_location = cmds.xform(f'{temp_poly}.vtx[1]', query = True, absolute = True, translation = True)
        to_delete(temp_poly)
        #cmds.delete(temp_poly)

        # Create Pole Vector control.
        temp_locator = cmds.spaceLocator(name = f'pv_{mid_joint_name}')
        cmds.xform(temp_locator, translation = pole_vector_location)

        if not pole_vector_parent:
            pole_vector_parent = ik_shoulder_ctrl
        
        pole_vector_control = create_control_for_joint(temp_locator[0], parent = pole_vector_parent, shape = 'sphere_rough', scale = [.04, .04, .04])[1] # dont need loc if temp locator is used? , loc = pole_vector_location
        ik_controls.append(pole_vector_control)
        to_delete(temp_locator)

        

        # Create line from ik mid joint to pole vector control
        #pole_vector_line = cmds.curve(p=[pole_vector_location, cmds.xform(bind_joint_mid, query = True, absolute = True, translation = True)],  d = 1)
        pole_vector_line = cmds.curve(name = f'pv_{mid_joint_name}_line', p=[(0,0,0), (1,0,0)],  d = 1)
        cmds.setAttr(f'{pole_vector_line}.template', 1)
        cmds.setAttr(f'{pole_vector_line}.overrideEnabled', 1)
        cmds.setAttr(f'{pole_vector_line}.lineWidth', 2)
        cmds.setAttr(f'{pole_vector_line}.overrideColor', 3)

        cluster1 = cmds.cluster( f'{pole_vector_line}.cv[0]')
        cluster2 = cmds.cluster( f'{pole_vector_line}.cv[1]')

        cluster1_shape = cmds.listRelatives(cluster1, type = 'shape')[0]
        cmds.setAttr(f'{cluster1_shape}.visibility', 0)
        cluster2_shape = cmds.listRelatives(cluster2, type = 'shape')[0]
        cmds.setAttr(f'{cluster2_shape}.visibility', 0)

        # Parent constraint clusters to control and ik mid joint (mo = False moves them)
        cmds.parentConstraint(ik_joints[1], cluster1, mo = False)
        cmds.parentConstraint(pole_vector_control, cluster2, mo = False)

        # Parent clusters and line in systems_group
        cmds.parent(cluster1[1], ik_setup_sys_group)
        cmds.parent(cluster2[1], ik_setup_sys_group)
        cmds.parent(pole_vector_line, ik_setup_sys_group)

        # Create empty group at pole vector location to parent to fk mid control for fkik matching.
        #mid_joint_name = bind_joint_mid[:(len(bind_joint_mid) - len(joint_suffix))]
        #print(f'mid_joint_name: {mid_joint_name}')
        #mid_joint_name = bind_joint_mid.remove(joint_suffix)
        # It's parented to pole vector here to match transforms too.
        mid_grp = cmds.group(name = f'fk_to_ik_target_{mid_joint_name}_grp', parent = pole_vector_control[0], empty = True)
        cmds.parentConstraint(fk_joints[1], mid_grp, mo = True)
        
        cmds.parent(mid_grp, ik_setup_sys_group)
        #thing = cmds.parentConstraint(pole_vector_control, mid_grp, maintainOffset = True)
        #cmds.parent(thing, constraints_group)

        # Create the constraint
        pole_vector_constraint = cmds.poleVectorConstraint(pole_vector_control, ik_handle[0])
        # move the pole vector constraint to the systems_group
        cmds.parent(pole_vector_constraint, ik_setup_sys_group)
        

        #Set visibility of IK controls
        for ik_ctrl in ik_controls:
            cmds.setDrivenKeyframe(f'{ik_ctrl[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 0, value = 1)
            cmds.setDrivenKeyframe(f'{ik_ctrl[0]}.visibility', currentDriver = f'{switch_control}.{attr_name}', driverValue = 1, value = 0)

        print(f'Finished create_2_jnt_ik_setup: {bind_joint_top}')

        """
        # Constraint the ik and fk to bind joints
        ikfk_joint_constraints = list()
        for i, bind_joint in enumerate(joint_list):
            ikfk_joint_constraints.append(cmds.parentConstraint(ik_joints[i], fk_joints[i], bind_joint, maintainOffset = True))
        
        # Create space switching attribute
        create_ik_fk_switch_attr(switch_control, ikfk_joint_constraints, fk_controls, ik_controls)
        """

        return [ik_joints, ik_controls], [fk_joints, fk_controls]
        
    except Exception as e:
        cmds.warning(f'     ##### Error: {e} #####')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    

"""
Added in ik setup
def create_ik_fk_switch_attr(control, ikfk_joint_constraints, fk_controls, ik_controls):
    '''
    arguments:
        control: The control that is getting the new attribute
        ikfk_joint_constraints: this is a list of parent constraints that was made to connect ik, fk controls to bind joints
        fk_controls: list of fk controls that change visability when other is active
        ik_controls: list of ik controls that change visability when other is active
    '''
    # maybe look into a calulating reversing ik to fk, and inverseing fk to ik, 
    # and the switch using strings and runs the proper method to switch
    #def switch_fk_to_ik(control):
    #def switch_ik_to_fk(control):

    switch_name = 'FK_IK'
    cmds.addAttr(control, longName = switch_name, defaultValue = 0, minValue = 0, maxValue = 1, attributeType = 'float', keyable = True)
    
    # Parent constriant weight driven key
    for constraint in ikfk_joint_constraints:
        attr_list = cmds.listAttr(constraint, keyable = True)
        fk_weight_attr = attr_list.pop()
        ik_weight_attr = attr_list.pop()

        cmds.setDrivenKeyframe(fk_weight_attr, currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 0, inTangentType = 'linear', outTangentType = 'linear')
        cmds.setDrivenKeyframe(fk_weight_attr, currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 1, inTangentType = 'linear', outTangentType = 'linear')

        cmds.setDrivenKeyframe(ik_weight_attr, currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 1, inTangentType = 'linear', outTangentType = 'linear')
        cmds.setDrivenKeyframe(ik_weight_attr, currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 0, inTangentType = 'linear', outTangentType = 'linear')

    # Visability driven key 
    for fk_ctrl in fk_controls:
        cmds.setDrivenKeyframe(f'{fk_ctrl}.visability', currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 0)
        cmds.setDrivenKeyframe(f'{fk_ctrl}.visability', currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 1)

    for ik_ctrl in ik_controls:
        cmds.setDrivenKeyframe(f'{ik_ctrl}.visability', currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 1)
        cmds.setDrivenKeyframe(f'{ik_ctrl}.visability', currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 0)
"""

def create_space_switching_attr(control, switch_with_1, switch_with_2 = None, switch_name = None):
    '''
    arguments:
        control: The control that is getting the new attribute
        switch_with_1: this is the attribute that is going to be driven with new attr
        switch_with_2: this is another attribute that is going to be driven with new attr, opposite 
        switch_name: Creates attr to this name
    return:
        The attribute's name
    '''
    '''
    # might use later for space switching (-1 is for one object, 0 is no influence, 1 is for another object?)
    if switch_with_2:
        min_value = -1
    else:
        min_value = 0
    '''
    cmds.addAttr(control, longName = switch_name, defaultValue = 0, minValue = 0, maxValue = 1, attributeType = 'float', keyable = True)
    cmds.setDrivenKeyframe(switch_with_1, currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 0, inTangentType = 'linear', outTangentType = 'linear')
    cmds.setDrivenKeyframe(switch_with_1, currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 1, inTangentType = 'linear', outTangentType = 'linear')
    
    # Second value is on by default
    if switch_with_2:
        # if using negative value, dv and v = 0, then dv = -1 and v = 1
        cmds.setDrivenKeyframe(switch_with_2, currentDriver = f'{control}.{switch_name}', driverValue = 0, value = 1, inTangentType = 'linear', outTangentType = 'linear')
        cmds.setDrivenKeyframe(switch_with_2, currentDriver = f'{control}.{switch_name}', driverValue = 1, value = 0, inTangentType = 'linear', outTangentType = 'linear')
        

def create_twist_joints(bind_joint_root, bind_joint_tip, num_of_twist_joints = 1, twist_joints = list()):
    '''
    arguments:
        bind_joint_root (string): joint 1 
        bind_joint_tip (string): joint 2
        num_of_twist_joints (int): amount of twist joints to make, 
        twist_joint_1 (string): if given a twist joint, don't generate one.
        twist_joint_2 (string): if given a twist joint, don't generate one.
    return:
        twist joint controls
    '''
    #eventually I will have to automate the twist joints so that they can be an option to add
    #based on wanting 1 or 2, then taking that and placing them in line of the upper to mid, and mid to lower

    twist_joints = twist_joints

    if not twist_joints:
        #create twist joints.
        #create a curve from joint 1 to joint 2
        #from that curve, split it between num_of_twist_joints
        #create joint from and place it on thoes points
        for t_jnt in range(num_of_twist_joints):
            twist_joints.append(cmds.joint())

    #create controls
    twist_joint_controls = list()
    for t_jnt in twist_joints:
        t_jnt_ctrl = create_control_for_joint(t_jnt, parent = bind_joint_root, shape = 'circle')[1]

    return twist_joint_controls


def auto_color_controls(controls_group):
    '''
    arguments:
        controls_group (string): The main controls group
    '''
    # for changing the controls color so left is blue, right is red, center is yellow
    right_controls = list()
    left_controls = list()
    center_controls = list()

    controls_in_group = [t for t in cmds.listRelatives(controls_group, allDescendents = True, type = 'transform') if control_suffix in t]
    temp_control_list = controls_in_group

    for ctrl in controls_in_group:
        if '_r' in ctrl:
            right_controls.append(temp_control_list.pop(ctrl))
    
    for ctrl in controls_in_group:
        if '_l' in ctrl:
            left_controls.append(temp_control_list.pop(ctrl))

    #these might do the same?
    '''
    [right_controls.append(temp_control_list.pop(ctrl)) for ctrl in controls_in_group if '_r' in ctrl]
    [left_controls.append(temp_control_list.pop(ctrl)) for ctrl in controls_in_group if '_l' in ctrl]
    '''

    center_controls = temp_control_list

    for ctrl in right_controls:
        change_color_controls(ctrl, 6)

    for ctrl in left_controls:
        change_color_controls(ctrl, 13)

    for ctrl in center_controls:
        change_color_controls(ctrl, 27)


def change_color_controls(control, color):
    '''
    arguments:
        control (String):   The control curve name that is being changed
        color (Int):        The color it is being changed to, represented in the color slider.
    '''
    cmds.setAttr(f'{control}.overrideEnabled', 1)
    cmds.setAttr(f'{control}.overrideColor', color)


def locator_to_joints(locator_group):
    '''
    adds and creates a hiearchy of joints in the locators position
    input: the height group that contains all the locators.
    returns: new joints
    '''
    locators = cmds.listRelatives(locator_group, allDescendents = True, type = 'transform')
    joint_group = cmds.group(name = 'joint' + group_suffix, empty = True)
    new_joints = list()
    
    #create joints at the world space of the locators, no scale.
    for locator in locators:
        joint_name = locator.replace(locator_suffix, '') + joint_suffix
        cmds.select(cl = True)
        new_joint = cmds.joint(name = joint_name)
        # Match transforms scale = False doesnt seem to work
        cmds.matchTransform(new_joint, locator, position = True, rotation = True, scale = False)
        #return
        #cmds.delete(new_joint, constructionHistory = True)
        new_joints.append(new_joint)
                
    for locator in locators:
        joint_name = locator.replace(locator_suffix, '') + joint_suffix
        locator_parent = cmds.listRelatives(locator, parent = True)[0]
        joint_parent_name = str(locator_parent.replace(locator_suffix, '') + joint_suffix)
        try:
            #print(f'Parenting {joint_name} to {joint_parent_name}')
            cmds.parent(joint_name, joint_parent_name)
        except Exception as e:
            #print(f'Exception expected: Parenting root_jnt to group.')
            cmds.parent(joint_name, joint_group)


    return joint_group
    #parent the joints in the same hiearchy as the locators.
    

def create_package_loc(name = 'package_loc_1', loc = [0, 0, 0], rot = [0, 0, 0], size = 0.3, width = 4):
    ''' Creates a package locator at a specific location. '''
    # Creating Curves
    curves = list()
    curves.append(cmds.curve(  p=[(0,0,0), (size,0,0)],  d = 1))
    curves.append(cmds.curve(  p=[(0,0,0), (0,size,0)],  d = 1))
    curves.append(cmds.curve(  p=[(0,0,0), (0,0,size)],  d = 1))

    for i, c in enumerate(curves):
        shape = cmds.listRelatives(c, children = True)[0]
        cmds.setAttr(f'{shape}.overrideEnabled', 1)
        cmds.setAttr(f'{shape}.lineWidth', width)

        if i == 0:
            cmds.setAttr(f'{shape}.overrideColor', 13)
        elif i == 1:
            cmds.setAttr(f'{shape}.overrideColor', 14)
        elif i == 2:
            cmds.setAttr(f'{shape}.overrideColor', 6)

    new_curve = combine_shapes(curves, name = name)
    # it was returning a shape, this returns the transform
    new_curve = cmds.listRelatives(new_curve, parent = True)
    #cmds.select(new_curve)
    #print(f'Creating loc: {name}: loc: {loc}, rot: {rot}')
    cmds.xform(new_curve, translation = loc, rotation = rot)
    cmds.select(cl = True)
    return new_curve


def combine_shapes(input_curves = None, name = 'curve'):
    ''' Combines a list of curves to a single curve. '''
    if not input_curves:
        input_curves = cmds.ls(sl = True)
        if len(input_curves) < 2:
            print('Nothing to combine.')
            input_curves = cmds.rename(input_curves, name)
            return input_curves

    curve_shape = cmds.listRelatives(input_curves, shapes = True)

    # Freeze Transforms, Delete History
    cmds.select(input_curves)
    cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
    cmds.delete(constructionHistory = True)

    # Transfering any values of the curve to the curve shape
    for ic in input_curves:
        cs = cmds.listRelatives(ic, shapes = True)
        line_width = cmds.getAttr(f'{ic}.lineWidth')
        override = cmds.getAttr(f'{ic}.overrideEnabled')
        color = cmds.getAttr(f'{ic}.overrideColor')
        for shape in cs:
            cmds.setAttr(f'{shape}.lineWidth', line_width)
            if override:
                cmds.setAttr(f'{shape}.overrideEnabled', override)
                cmds.setAttr(f'{shape}.overrideColor', color)
    
    # Parent shape to last transform node.
    for i in range(len(curve_shape)-1):   
        cmds.parent(curve_shape[i], input_curves[-1], add = True, shape = True)
        #cmds.rename(curve_shape[i], f'{name}Shape')
        #cmds.select(input_curves[-1], replace = True)

    # Clean and return curve
    # output_curve = input_curves.pop() returned old name :/
    cmds.rename(input_curves[-1], name)
    input_curves.pop()
    output_curve = cmds.ls(sl = True)[0]
    #print(f'Selecting {input_curves} to delete.')
    to_delete(input_curves)
    #cmds.select(input_curves)
    #cmds.delete()
    cmds.select(cl = True)
    return output_curve


def poly_to_ctrl(poly = None, name = 'curve'):
    ''' Converts a polygon's edges to a single curve. '''
    if not poly:
        try:
            poly = cmds.ls(sl=True)[0]
        except:
            print('Nothing to run.')
            return

    cmds.select(poly)
    edge_num = cmds.polyEvaluate(e=True)
    new_curves = list()

    for edge_index in range(edge_num):
        edge = f'{poly}.e[{edge_index}]'
        cmds.select(edge)
        new_curve = cmds.polyToCurve(form=3,degree=1)[0]
        #cmds.delete(constructionHistory = True)
        new_curves.append(new_curve)
    
    output_curve = combine_shapes(new_curves, name)
    
    # Center Pivot
    cmds.select(output_curve)
    cmds.xform(centerPivots = 1)
    cmds.select(cl = True)
    to_delete(poly)
    #cmds.delete(poly)

    return output_curve


def reset_to_world(object = None):
    ''' Resets the tranforms of an object back to world space. '''
    if not object:
        try:
            object = cmds.ls(sl=True)[0]
        except:
            print('Nothing to run.')
            return
    
    locator = cmds.spaceLocator()
    cmds.matchTransform(locator, object)
    cmds.parent(object, locator)

    # Freeze Transforms, Delete History
    cmds.select(object)
    cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
    cmds.delete(constructionHistory = True)

    cmds.parent(object, world = True)
    to_delete(locator)
    cmds.delete(locator)
    cmds.select(cl = True)


def lock_attr(attr_list, hide = False):
    ''' 
    Arguments:
        args (list(Strings)): list of attributes to lock
    '''

    for attr in attr_list:
        try:
            cmds.setAttr(attr, lock = True)
            if hide:
                cmds.setAttr(attr, keyable = False)
        except:
            print(f"Attribute doesn't exist: {attr}")


"""
#add multiple curves/parenting (eye controls)
def old_export_ctrl_shape(control_to_export = None):
    ''' 
    Export Control to json or xml. 
    Arguments:
        control_to_export (string): The name of the shape being exported, or control shape selected
    '''
    if not control_to_export:
        try:
            control_to_export = cmds.ls(sl=True)[0]
            test_shape = cmds.listRelatives(control_to_export, shapes = True)[0]
            cmds.getAttr(f'{test_shape}.cv[*]')    
        except:
            print('Nothing to run or not a valid object.')
            return
	
    file_name = control_to_export + '.json'
    files_in_path = os.listdir(script_path+'/rc_tools/curves/')

    #check if the data already exists and warn that it's going to overwrite
    if file_name in files_in_path:
        # OLD is a folder where things are moved
        if file_name == 'OLD':
            cmds.warning('OLD is not a valid name, change it!')
            return
        confirm = cmds.confirmDialog(title = 'Control already exists!!', message = 'This will overwrite the existing file.', button = ['Overwrite', 'Cancel'], cancelButton = 'Cancel')
        print(confirm)
        if confirm == 'Cancel':
            return
        else:
            #Move file instead of overwriting for now
            counter = 1
            destination = f'{script_path}/rc_tools/curves/OLD/{control_to_export}.json'
            while os.path.exists(destination):
                destination = f'{script_path}/rc_tools/curves/OLD/{control_to_export}-{counter}.json'
                counter += 1
            os.rename(f'{script_path}/rc_tools/curves/{file_name}', destination)

    # Freeze Transforms, Delete History
    cmds.select(control_to_export, hierarchy = True)
    cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
    cmds.delete(constructionHistory = True)
    cmds.select(clear = True)

    data = dict()

    cmds.select(control_to_export, hierarchy = True)
    controls = cmds.ls(sl = True, type = 'transform')
    cmds.select(cl = True)
    
    shapes = cmds.listRelatives(control_to_export, shapes=True)

    data['transform'] = control_to_export
    data['shapes'] = list()

    for shape in shapes:
        shape_data = dict()
        shape_data['shape'] = shape
        shape_data['degree'] = cmds.getAttr(f'{shape}.degree')
        shape_data['points']  = cmds.getAttr(f'{shape}.cv[*]')
        shape_data['form']  = cmds.getAttr(f'{shape}.form')
        shape_data['override']  = cmds.getAttr(f'{shape}.overrideEnabled')
        shape_data['color']  = cmds.getAttr(f'{shape}.overrideColor')
        shape_data['line_width']  = cmds.getAttr(f'{shape}.lineWidth')

        data['shapes'].append(shape_data)

    with open(script_path+'/rc_tools/curves/' + file_name, 'w') as out_file:
        json.dump(data, out_file, indent = 4)

    print(f'Exported: {file_name}')
"""
"""
def old_import_ctrl_shape(control_to_import, loc = (0,0,0), rot = (0,0,0), scale = (1, 1, 1)):
    '''
    Import Control from json or xml. 
    Arguments:
        control_to_import (string): The name of the shape being imported
    returns: 
        The curve imported.
    '''
    control_to_import = control_to_import + '.json'
    rc_curves = os.listdir(script_path+'/rc_tools/curves/')

    if control_to_import not in rc_curves or control_to_import == 'OLD': 
        print(f'{control_to_import} not in folder')
        return

    # Storing file to data
    with open(script_path+'/rc_tools/curves/' + control_to_import, 'r') as f:
        data = json.load(f)
    
    # Creating the curve
    curve_shape_list = list()
    for curve_shape in data['shapes']:
        crv = cmds.curve(p = curve_shape['points'], degree = curve_shape['degree'])
        cmds.setAttr(f'{crv}.overrideEnabled', curve_shape['override'])
        cmds.setAttr(f'{crv}.overrideColor', curve_shape['color'])
        cmds.setAttr(f'{crv}.lineWidth', curve_shape['line_width'])
        
        # If the shape is periodic, the shape is closed.
        if curve_shape['form'] == 2:
            cmds.closeCurve(crv, preserveShape = 0, constructionHistory = False, replaceOriginal = True)
        
        crv = cmds.rename(crv, curve_shape['shape'])
        curve_shape_list.append(crv)
    
    output_curve = combine_shapes(curve_shape_list, data['transform'])
    return output_curve
"""

def export_ctrl_shape(control_to_export = None, screenshot = False):
    ''' 
    Export Control to json or xml. 
    Arguments:
        control_to_export (string): The name of the shape being exported, or control shape selected
        screenshot (boolean): If the control is screenshotted
    '''
    if not control_to_export:
        try:
            control_to_export = cmds.ls(sl=True)[0]
            test_shape = cmds.listRelatives(control_to_export, shapes = True)[0]
            cmds.getAttr(f'{test_shape}.cv[*]')    
        except:
            print('Nothing to run or not a valid object.')
            return
	
    file_name = control_to_export + '.json'
    files_in_path = os.listdir(script_path+'/rc_tools/curves/')

    #check if the data already exists and warn that it's going to overwrite
    if file_name in files_in_path:
        # OLD is a folder where things are moved
        if file_name == 'OLD':
            cmds.warning('OLD is not a valid name, change it!')
            return
        confirm = cmds.confirmDialog(title = 'Control already exists!!', message = 'This will overwrite the existing file.', button = ['Overwrite', 'Cancel'], cancelButton = 'Cancel')
        print(confirm)
        if confirm == 'Cancel':
            return
        else:
            #Move file instead of overwriting for now
            counter = 1
            destination = f'{script_path}/rc_tools/curves/OLD/{control_to_export}.json'
            while os.path.exists(destination):
                destination = f'{script_path}/rc_tools/curves/OLD/{control_to_export}-{counter}.json'
                counter += 1
            os.rename(f'{script_path}/rc_tools/curves/{file_name}', destination)

    # Freeze Transforms, Delete History
    cmds.select(control_to_export, hierarchy = True)
    cmds.makeIdentity(apply = 1, translate = 1, rotate = 1, scale = 1, normal = 0)
    cmds.delete(constructionHistory = True)
    cmds.select(clear = True)

    # Data storage for root shape
    data = dict()
    data['root_transform'] = control_to_export
    data['root_shapes'] = list()
    root_shapes = cmds.listRelatives(control_to_export, shapes=True)

    for shape in root_shapes:
        root_shape_data = dict()
        root_shape_data['shape'] = shape
        root_shape_data['degree'] = cmds.getAttr(f'{shape}.degree')
        root_shape_data['points']  = cmds.getAttr(f'{shape}.cv[*]')
        root_shape_data['form']  = cmds.getAttr(f'{shape}.form')
        root_shape_data['override']  = cmds.getAttr(f'{shape}.overrideEnabled')
        root_shape_data['color']  = cmds.getAttr(f'{shape}.overrideColor')
        root_shape_data['line_width']  = cmds.getAttr(f'{shape}.lineWidth')
        data['root_shapes'].append(root_shape_data)
    
    # Data storage for child objects
    data['child_transforms'] = list()
    child_controls = cmds.listRelatives(control_to_export, children = True, type = 'transform')
    if  child_controls:

        for cc in child_controls:
            child_data = dict()
            child_shapes = cmds.listRelatives(cc, shapes=True)

            child_data['transform'] = cc
            child_data['parent'] = cmds.listRelatives(cc, parent=True)[0]
            child_data['shapes'] = list()

            for shape in child_shapes:
                shape_data = dict()
                shape_data['shape'] = shape
                shape_data['degree'] = cmds.getAttr(f'{shape}.degree')
                shape_data['points']  = cmds.getAttr(f'{shape}.cv[*]')
                shape_data['form']  = cmds.getAttr(f'{shape}.form')
                shape_data['override']  = cmds.getAttr(f'{shape}.overrideEnabled')
                shape_data['color']  = cmds.getAttr(f'{shape}.overrideColor')
                shape_data['line_width']  = cmds.getAttr(f'{shape}.lineWidth')
                child_data['shapes'].append(shape_data)

            data['child_transforms'].append(child_data)

    # Screenshotting the icon
    if screenshot:
        cmds.select(cl = True)
        cmds.showHidden(control_to_export)
        cmds.viewFit(control_to_export)
        cmds.playblast(completeFilename = f'{script_path}/rc_tools/icons/{control_to_export}.jpg', frame = 0, format = "image", viewer = False, widthHeight = [400, 400], showOrnaments = False)
    
    # Saving data to json
    with open(script_path+'/rc_tools/curves/' + file_name, 'w') as out_file:
        json.dump(data, out_file, indent = 4)
    print(f'Exported: {file_name}')


def import_ctrl_shape(control_to_import, name = None, loc = [0,0,0], rot = [0,0,0], loc_shape = [0,0,0], rot_shape = [0,0,0], scale_shape = [1,1,1], num_of_group = 0, add_suffix = True):
    '''
    Import Control from json. 
    Arguments:
        control_to_import (string): The name of the shape being imported
        name (string): Name of the control
        loc(set(int)): Where the most parent object is moved to.
        rot(set(int)): Where the most parent object is rotated to.
        scale(set(int)): Where the control shape is scaled to. (scale the cv's to the object)
        num_of_group (int):
    returns: 
        List of groups, list of curves.
    '''
    try:
        control_file = control_to_import + '.json'
        rc_curves = os.listdir(script_path+'/rc_tools/curves/')

        # Since json is added in control_file, might not need to check for old
        if control_file not in rc_curves or control_file == 'OLD': 
            print(f'{control_file} not in folder')
            return

        # Storing file data to data
        with open(script_path+'/rc_tools/curves/' + control_file, 'r') as f:
            data = json.load(f)
        
        if not name:
            name = control_to_import

        # Creating groups
        print(f'Importing control: {control_to_import}')
        output_groups = list()
        if num_of_group:
            group_name = name
            if add_suffix: group_name = group_name + group_suffix
            root_grp = cmds.group(name = group_name, empty = True)
            output_groups.append(root_grp)
            parent = root_grp
            if num_of_group > 1:
                for i in range(num_of_group - 1):
                    group_name = name + f'_{i+1}'
                    if add_suffix: group_name = group_name + group_suffix
                    new_grp = cmds.group(name = group_name, empty = True, parent = parent)
                    parent = new_grp
        #print(f'Groups created: {output_groups}')
        #check if something is selected.
        selected = cmds.ls(sl = True)
        if selected and loc != (0,0,0) and rot != (0,0,0):
            loc = cmds.xform(selected[0], query = True, translation = True, worldSpace = True)
            rot = cmds.xform(selected[0], query = True, rotation = True, worldSpace = True)

        # Creating the curve
        output_curve = list()
        curve_shape_list = list()
        for curve_shape in data['root_shapes']:
            crv = cmds.curve(p = curve_shape['points'], degree = curve_shape['degree'])
            cmds.setAttr(f'{crv}.overrideEnabled', curve_shape['override'])
            cmds.setAttr(f'{crv}.overrideColor', curve_shape['color'])
            cmds.setAttr(f'{crv}.lineWidth', curve_shape['line_width'])

            # If the shape is periodic, the shape is closed.
            if curve_shape['form'] == 2:
                cmds.closeCurve(crv, preserveShape = 0, constructionHistory = False, replaceOriginal = True)
            
            crv = cmds.rename(crv, curve_shape['shape'])
            curve_shape_list.append(crv)
            #print(f"Created: {curve_shape['shape']}")
        
        # Even if theres one curve, it will be renamed
        #print('before combineing shapes')
        curve_name = name or data['root_transform']
        if add_suffix: curve_name = curve_name + control_suffix
        output_curve.append(combine_shapes(curve_shape_list, curve_name))
        #print('after combineing shapes')
        
        #print(f"Working on child curve: {data['child_transforms']}")
        for child_transform in data['child_transforms']:
            curve_shape_list = list()
            #print(f"Working on: {child_transform['transform']}")
            for curve_shape in child_transform['shapes']:
                crv = cmds.curve(p = curve_shape['points'], degree = curve_shape['degree'])
                cmds.setAttr(f'{crv}.overrideEnabled', curve_shape['override'])
                cmds.setAttr(f'{crv}.overrideColor', curve_shape['color'])
                cmds.setAttr(f'{crv}.lineWidth', curve_shape['line_width'])
                
                # If the shape is periodic, the shape is closed.
                if curve_shape['form'] == 2:
                    cmds.closeCurve(crv, preserveShape = 0, constructionHistory = False, replaceOriginal = True)
                
                crv = cmds.rename(crv, curve_shape['shape'])
                curve_shape_list.append(crv)
        
            # Even if theres one curve, it will be renamed
            curve_name = child_transform['transform']
            if add_suffix: curve_name = curve_name + control_suffix
            child_curve = combine_shapes(curve_shape_list, curve_name)
            cmds.xform(child_curve, centerPivots = True)
            
            # make sure that the child_transform parent is an object created here instead of going to another object.
            parent = None
            for transform in output_curve:
                #print(f"Testing: {transform} > {child_transform['parent']}")
                parent = transform
                if child_transform['parent'] in transform:
                    break

            #print(f'Parent: {parent}')
            if parent:
                cmds.parent(child_curve, parent)
            output_curve.append(child_curve)
        #print('Finished all shapes')

        #Scale the control vertices of all the curves
        #cmds.select(output_curve[0], hierarchy = True)
        #selected = cmds.ls(sl = True)
        cmds.select(cl = True)
        for thing in output_curve:
            cmds.select(f'{thing}.cv[*]', add = True)
        #cmds.scale(scale_shape, scale_shape, scale_shape, centerPivot = True)
        cmds.xform(scale = scale_shape, relative = True)
        cmds.xform(rotation = rot_shape, relative = True)
        cmds.xform(translation = loc_shape, relative = True)
        # OG cmds.xform(translation = loc_shape, rotation = rot_shape, scale = scale_shape, relative = True)
        cmds.select(cl = True)
        #print('Finished scaling')

        # Center pivots of child curves.
        '''
        not sure why but this breaks everything
        if output_curve > 1:
            print(f'{output_curve} > 1')
            for thing in selected[1:]:
                cmds.xform(thing, centerPivots = 1) 
        print('Finished center pivoting')
        '''
        # Parent curve to group and move to loc and rot
        #print(f'rot: {rot}     loc: {loc}')
        if num_of_group:
            cmds.parent(output_curve[0], output_groups[-1])
            # Rotation first
            cmds.xform(output_groups[0], rotation = rot)
            cmds.xform(output_groups[0], translation = loc)
            #print('Finished group parenting and transforming')
        else:
            cmds.xform(output_curve[0], rotation = rot)
            cmds.xform(output_curve[0], translation = loc)
            #print('Finished curve transforming')
        
        if output_groups:
            return output_groups, output_curve
        else:
            return output_curve
    except Exception as e:
        cmds.warning(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def joints_to_locators():
    #takes joints and places a package loc on each, rename, parent them according to the joints selected
    joints = cmds.ls(sl = True, type = 'joint')
    new_locs = list()

    for j in joints:
        loc_name = str(j + locator_suffix)
        temp_loc = create_package_loc(name = loc_name)
        cmds.matchTransform(temp_loc, j)
        #temp_loc = cmds.rename(temp_loc, str('loc_'+j))
        new_locs.append(temp_loc)
        
    for j in joints:
        loc_name = str(j + locator_suffix)
        joint_parent = cmds.listRelatives(j, parent = True)[0]
        loc_parent_name = str(joint_parent + locator_suffix)
        print(f'Joint: {j},    Parent: {joint_parent}')
        try:   
            cmds.parent(loc_name, loc_parent_name)
        except Exception as e:
            print(f'################ Error: {e}')

    return new_locs


# take package locators and store it in a json file that can be read from later.
def export_rig_setup(name, height_cm, package_locators = None):

    if not package_locators:
        try:
            package_locators = cmds.ls(sl=True)
        except:
            print('Nothing to run.')
            return

    path = f'{script_path}/rc_tools/rig locators/{name}.json'

    data = dict()
    data['name'] = name
    data['height_cm'] = height_cm
    data['loc'] = list()

    for locators in package_locators:

        # Gets amount ov control verticies
        #cvs = cmds.getAttr(f'{cmds.listRelatives(cmds.ls(locators), shapes = True)[0]}.cp', size = True)
        #or
        #spans = cmds.getAttr(f'{cmds.listRelatives(cmds.ls(locators), shapes = True)[0]}.spans')
        #degree = cmds.getAttr(f'{cmds.listRelatives(cmds.ls(locators), shapes = True)[0]}.degree')
        #cvs = spans + degree

        # Get size of locator
        size = 0    
        for i in range(3):
            size = size + cmds.xform(f'{cmds.listRelatives(cmds.ls(locators), shapes = True)[0]}.cv[1]', query = True, t = True)[i]

        loc_data = dict()
        loc_data['name'] = str(locators)
        loc_data['loc'] = [round(t, 10) for t in cmds.xform(locators, query = True, translation = True, worldSpace = True)]
        loc_data['rot'] = [round(t, 10) for t in cmds.xform(locators, query = True, rotation = True, worldSpace = True)]
        loc_data['size'] = size
        loc_data['width'] = cmds.getAttr(f'{cmds.listRelatives(cmds.ls(locators), shapes = True)[0]}.lineWidth')
        try:
            loc_data['parent'] = cmds.listRelatives(locators, parent = True)[0]
        except:
            loc_data['parent'] = None
            print(f'{locators} has no parent.')

        data['loc'].append(loc_data)
        

    with open(path, 'w') as out_file:
        json.dump(data, out_file, indent = 4)
    
    print('Rig Exported')


def import_rig_setup(name):
    path = f'{script_path}/rc_tools/rig locators/{name}.json'

    with open(path, 'r') as in_file:
        data = json.load(in_file)

    
    height_grp = cmds.group(name = f'{data["name"]}_height_scale_grp', em=True)
    # Place locators in cm (maybe change to read json file, set to units used?)
    current_unit = cmds.currentUnit(query = True)
    cmds.currentUnit( linear='cm')

    created_locators = list()

    for locator in data['loc']:
        #print(f'Loc data    : {locator["name"]}: loc: {locator["loc"]}, rot: {locator["rot"]}')
        print(f'Creating {locator["name"]} locator.')
        #print(f'LOC: {locator["loc"]} ROT: {locator["rot"]}.')
        rig_loc = create_package_loc(name = locator['name'], size = locator['size'], width = locator['width'])
        #print(rig_loc)
        #rig_loc = create_package_loc(name = locator['name'], loc = locator['loc'], rot = locator['rot'], size = locator['size'], width = locator['width'])
        cmds.xform(rig_loc, translation = locator['loc'], rotation = locator['rot'])
        created_locators.append(rig_loc)

    # Parenting locators and finding root (root loc doesnt have a parent)
    loc_root = list()
    for locator in data['loc']:
        if locator['parent']:
            cmds.parent(locator['name'], locator['parent'])
        else:
            loc_root.append(locator['name'])

    #take rig height and convert to current unit
    converted_height = data['height_cm']

    if current_unit == 'm':
        converted_height = converted_height / 100
    elif current_unit == 'in':
        converted_height = converted_height / 2.54
    elif current_unit == 'ft':
        converted_height = converted_height / 30.48

    # Get scale by 
    set_height = cmds.floatFieldGrp(rc_height_field, query = True, value1 = True)
    scale = set_height / converted_height
    print(f'Setup hight scale set to {scale}: {converted_height * scale}.')

    # set back to scene units
    cmds.currentUnit( linear=current_unit)

    cmds.parent(loc_root, height_grp)
    cmds.xform(height_grp, scale = [scale, scale, scale])

    return height_grp


def change_package_locator(locators = None, size = None, width = None, scale = None):
    if not locators:
        try:
            locators = cmds.ls(sl=True)
        except:
            print('Nothing to run.')
            return
        
    for locator in locators:
        for curve in cmds.listRelatives(cmds.ls(locator), shapes = True):

            if size:
                translation = [0, 0, 0]

                for i in range(3):
                    get_t = cmds.xform(f'{curve}.cv[1]', query = True, t = True)[i]
                    if get_t:
                        translation[i] = size

                cmds.xform(f'{curve}.cv[1]', t = translation)
            if width:
                cmds.setAttr(f'{curve}.lineWidth', width)
            if scale:
                current_size = cmds.xform(f'{curve}.cv[1]', query = True, t = True)[i]
                translation = [0, 0, 0]

                for i in range(3):
                    get_t = cmds.xform(f'{curve}.cv[1]', query = True, t = True)[i]
                    if get_t:
                        translation[i] = size
                









'''
def change_package_locator_width(width, locators = None):
    if not locators:
        try:
            locators = cmds.ls(sl=True)
        except:
            print('Nothing to run.')
            return
        
    for locator in locators:
        for curve in cmds.listRelatives(cmds.ls(locator), shapes = True):
            cmds.setAttr(f'{curve}.lineWidth', width)
'''

'''
Skin weight data< check out:
https://www.aganimator.com/tutorials/2016/2/19/saving-mayas-skin-weights-to-json
'''


#run the script        
rc_tool()


#export_rig_setup('biped', 180, package_locators = joints_to_locators())
#export_rig_setup('biped', 180)
#change_package_locator(size = 1.5, width = 3)
#locator_to_joints('biped_height_scale_grp')

'''
# For importing all controls
curve_locations = script_path+'/rc_tools/curves/'
dir_list = os.listdir(curve_locations)
for f in dir_list:
    things = f.replace('.json', '')
    if things != 'OLD':
        import_ctrl_shape(things)
'''

#export_ctrl_shape()
#curves = import_ctrl_shape('package_loc')
#curves = cmds.ls(sl=True)
#combine_shapes(curves, 'package_loc')
#poly_to_ctrl()

#combine_shapes()

#export_ctrl_shape()

#import_ctrl_shape()


#export_rig_setup('biped', 180)
#change_package_locator(size = 1.5, width = 3)
#joints_to_locators()








"""
import sys
import time
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Pyside2 Simple Appplication")
        self.setGeometry(300,300, 500,400)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)
 
 
myApp = QApplication(sys.argv)
window = Window()
window.show()
 
time.sleep(3)
window.resize(600,400)
#window.repaint()
 
myApp.exec_()
sys.exit(0)






# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), 'rc_tools', 'rc_tools.ui')
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = MyMainWindow()
    widget.show()
    sys.exit(app.exec_())
"""
