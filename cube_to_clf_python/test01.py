import PyOpenColorIO as OCIO

try:
   config = OCIO.GetCurrentConfig()
   processor = config.getProcessor(OCIO.ROLE_COMPOSITING_LOG,
                                   OCIO.ROLE_SCENE_LINEAR)
   cpu = processor.getDefaultCPUProcessor()

   # Apply the color transform to the existing RGBA pixel data
   img = [1, 0, 0, 0]
   img = cpu.applyRGBA(img)
except Exception as e:
   print("OpenColorIO Error: ", e)