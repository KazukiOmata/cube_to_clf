import PyOpenColorIO as OCIO

def lut_to_clf(input_lut_file, output_clf_file):
    # 読み込むLUTファイルのパス

    # OCIOの設定を初期化
    config = OCIO.Config.CreateRaw()

    # 入力カラースペースを定義
    input_color_space = "InputColorSpace"
    config.addColorSpace(OCIO.ColorSpace(name=input_color_space))

    # 出力カラースペースを定義
    output_color_space = "OutputColorSpace"
    config.addColorSpace(OCIO.ColorSpace(name=output_color_space))

    # ルックアップテーブルを定義
    lut = OCIO.FileTransform()
    lut.setSrc(input_lut_path)
    lut.setInterpolation(OCIO.INTERP_LINEAR)

    # ルックアップテーブルを追加
    config.addColorSpace(OCIO.ColorSpace(name="LUTSpace", transforms=[lut]))

    # 入力・出力変換を定義
    transform = OCIO.GroupTransform()
    transform.push_back(OCIO.FileTransform(src=input_lut_path))
    transform.push_back(OCIO.ColorSpaceTransform(src=input_color_space, dst=output_color_space))

    # ルックアップテーブルを追加
    config.addColorSpace(OCIO.ColorSpace(name="LUTSpace_1", transforms=[transform]))

    # CLFファイルに出力
    config.serialize(output_clf_path)

    print("CLF file has been successfully created:", output_clf_path)

# LUTファイルからCLFファイルへの変換を実行


input_lut_path = "/Users/omakazu/program/01_multi_project/003_make_CLF/cube_to_clf/cube_LUT/ARRI_LogC3-to-Gamma24_Rec709_D65-v1_33.cube"  # ファイルの実際のパスに置き換える

    # 書き出すCLFファイルのパス
output_clf_path = "/Users/omakazu/program/01_multi_project/003_make_CLF/cube_to_clf/CLF/file.clf"  # ファイルの実際のパスに置き換える

lut_to_clf(input_lut_path, output_clf_path)