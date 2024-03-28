import PyOpenColorIO as OCIO


try:
   config = OCIO.GetCurrentConfig()
   #
   # display = config.getDefaultDisplay()
   # view = config.getDefaultView(display)
   # processor = config.getProcessor(OCIO.ROLE_SCENE_LINEAR, display, view, OCIO.TRANSFORM_DIR_FORWARD)
   #
   #
   # # processor = config.getProcessor(OCIO.ROLE_COMPOSITING_LOG,
   # #                                 OCIO.ROLE_SCENE_LINEAR)
   # cpu = processor.getDefaultCPUProcessor()
   #
   #
   #
   #
   #
   # # Apply the color transform to the existing RGBA pixel data
   # # img = [1, 0, 0, 0]
   # img = [1,0,0]
   # img = cpu.applyRGBA(img)
except Exception as e:
   print("OpenColorIO Error: ", e)


# https://opencolorio.readthedocs.io/projects/config-aces/en/latest/generated/opencolorio_config_aces.generate_clf_transform.html#opencolorio_config_aces.generate_clf_transform
# https://opencolorio.readthedocs.io/projects/config-aces/en/latest/opencolorio_config_aces.clf.html
# opencolorio_config_aces.generate_clf_transform()
