#At my ITS job, documentation is absolutely necessary, and must follow a certain standard
#This program is to automate the most basic parts of documentation that are uniform
#amongst most cases

#Although it is basic and known procedure, just to avoid any kind of revealing information,
#I have replaced the actual verification step with "V-Step #1", "V-Step #2", etc.

#V-Step #4 is a failsafe if either step 2 or 3 do not work. That is why it is coded that way.
attemptnum = int(input("Enter attempt number: "))
if attemptnum == 1:
    attemptlabel = "First attempt"
elif attemptnum == 2:
    attemptlabel = "Second attempt"
elif attemptnum == 3:
    attemptlabel = "Third attempt"
else:
    print("error")
    attemptlabel = "error"
idverify = str(input("ID Verification Needed? (Y/N) "))
if idverify in ("Y", "y"):
    idverify1 = str(input("V-Step #1? (Y/N) "))
    if idverify1 in ("Y", "y"):
        idverify2 = str(input("V-Step #2? (Y/N) "))
        if idverify2 in ("Y", "y"):
            idverify3 = str(input("V-Step #3? (Y/N) "))
            if idverify3 in ("Y", "y"):
                print(attemptlabel,
                      "Information Verified\n"
                      "V-Step #1: Y\n"
                      "V-Step #2: Y\n"
                      "V-Step #3: Y",
                      sep="\n")
            elif idverify3 in ("N", "n"):
                zoomcall = str(input("V-Step #4? (Y/N) "))
                if zoomcall in ("Y", "y"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: Y\n"
                          "V-Step #2: Y\n"
                          "V-Step #3: N\n" 
                          "V-Step #4: Y",
                          sep="\n")
                elif zoomcall in ("N", "n"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: Y\n"
                          "V-Step #2: Y\n"
                          "V-Step #3: N\n"
                          "V-Step #4: N",
                          sep="\n")
                else:
                    print("error")
            else:
                print("error")
        elif idverify2 in ("N", "n"):
                zoomcall = str(input("V-Step #4? (Y/N) "))
                if zoomcall in ("Y", "y"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: Y\n"
                          "V-Step #2: N\n"
                          "V-Step #3: N\n"
                          "V-Step #4: Y",
                          sep="\n")
                elif zoomcall in ("N", "n"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: Y\n"
                          "V-Step #2: N\n"
                          "V-Step #3: N\n"
                          "V-Step #4: N",
                          sep="\n")
                else:
                    print("error")
        else:
            print("error")
    elif idverify1 in ("N", "n"):
                zoomcall = str(input("V-Step #4? (Y/N) "))
                if zoomcall in ("Y", "y"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: N\n"
                          "V-Step #2: N\n"
                          "V-Step #3: N\n"
                          "V-Step #4: Y",
                          sep="\n")
                elif zoomcall in ("N", "n"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "V-Step #1: N\n"
                          "V-Step #2: N\n"
                          "V-Step #3: N\n"
                          "V-Step #4: N",
                          sep="\n")
                else:
                    print("error")
    else:
        print("error")
elif idverify in ("N", "n"):
    print(attemptlabel,
         "ID Verification not needed",
          sep="\n")
else:
    print("error")
