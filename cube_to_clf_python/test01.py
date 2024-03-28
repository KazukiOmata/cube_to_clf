

import PyOpenColorIO as OCIO


try:
    config = OCIO.GetCurrentConfig()
    processor = config.getProcessor(OCIO.Constants.ROLE_COMPOSITING_LOG,
                                    OCIO.Constants.ROLE_SCENE_LINEAR)

    # Apply the color transform to the existing RGBA pixel data
    img = processor.applyRGBA(img)
except Exception, e:
    print "OpenColorIO Error",e