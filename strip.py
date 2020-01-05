if __name__ == "__main__":
    src = "b.txt"
    dst = "resources-min.txt"
    with open(src, "r", encoding="utf-8") as srcFile:
        srcLines = srcFile.readlines()
        dstLines = []
        for srcLine in srcLines:
            if srcLine not in dstLines:
                dstLines.append(srcLine)

        with open(dst, "w", encoding="utf-8") as dstFile:
            dstFile.writelines(dstLines)

        print(f"Selected {len(dstLines)} lines from {src} to {dst}")
