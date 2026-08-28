from service import visible_titles
if __name__=="__main__":
    import sys
    print(visible_titles(sys.argv[1] if len(sys.argv)>1 else ""))
