def CallScript():
    idverify = str(input("ID Verification Needed? (Y/N) "))
    if idverify in ("Y", "y"):
        idverify1 = str(input("Step 1? (Y/N) "))
        if idverify1 in ("Y", "y"):
            idverify2 = str(input("Step 2? (Y/N) "))
            if idverify2 in ("Y", "y"):
                idverify3 = str(input("Step 3? (Y/N) "))
                if idverify3 in ("Y", "y"):
                    print(attemptlabel,
                          "Information Verified\n"
                          "Step 1: Y\n"
                          "Step 2: Y\n"
                          "Step 3: Y",
                          sep="\n")
                elif idverify3 in ("N", "n"):
                    zoomcall = str(input("Was ID verified on zoom call? (Y/N) "))
                    if zoomcall in ("Y", "y"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: Y\n"
                              "Step 2: Y\n"
                              "Step 3: N\n"
                              "Zoom: Y - Verified Govt ID",
                              sep="\n")
                    elif zoomcall in ("N", "n"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: Y\n"
                              "Step 2: Y\n"
                              "Step 3: N\n"
                              "Zoom: N - Unable to Verify Govt ID",
                              sep="\n")
                    else:
                        print("error")
                else:
                    print("error")
            elif idverify2 in ("N", "n"):
                    zoomcall = str(input("Was ID verified on zoom call? (Y/N) "))
                    if zoomcall in ("Y", "y"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: Y\n"
                              "Step 2: N\n"
                              "Step 3: N\n"
                              "Zoom: Y - Verified Govt ID",
                              sep="\n")
                    elif zoomcall in ("N", "n"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: Y\n"
                              "Step 2: N\n"
                              "Step 3: N\n"
                              "Zoom: N - Unable to Verify Govt ID",
                              sep="\n")
                    else:
                        print("error")
            else:
                print("error")
        elif idverify1 in ("N", "n"):
                    zoomcall = str(input("Was ID verified on zoom call? (Y/N) "))
                    if zoomcall in ("Y", "y"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: N\n"
                              "Step 2: N\n"
                              "Step 3: N\n"
                              "Zoom: Y - Verified Govt ID",
                              sep="\n")
                    elif zoomcall in ("N", "n"):
                        print(attemptlabel,
                              "Information Verified\n"
                              "Step 1: N\n"
                              "Step 2: N\n"
                              "Step 3: N\n"
                              "Zoom: N - Unable to Verify Govt ID",
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


restart = "Y"
while restart in ("Y", "y"):
    complete = False
    while not complete:
        try:
            attemptnum = int(input("Enter attempt number: "))
        except ValueError:
            print("error")
            continue

        if attemptnum == 1:
            attemptlabel = "First attempt"
        elif attemptnum == 2:
            attemptlabel = "Second attempt"
        elif attemptnum == 3:
            attemptlabel = "Third attempt"
        else:
            print("error")
            continue

        answer = str(input("Did you call? (Y/N)"))
        if answer in ("Y", "y"):
            callanswer = str(input("Did they answer?"))
            if callanswer in ("Y", "y"):
                CallScript()
                complete = True
            elif callanswer in ("N", "n") and attemptnum == 1:
                print(attemptlabel,
                      "Called user at number listed\n"
                      "Left VM\n"
                      "Will make second attempt in 2 hours",
                      sep="\n")
                complete = True
            elif callanswer in ("N", "n"):
                print(attemptlabel,
                      "Called user at number listed\n"
                      "Left VM\n"
                      "Sent email at email listed\n"
                      "Will make another attempt in 2 hours",
                      sep="\n")
                complete = True
            else:
                print("error")
        elif answer in ("N", "n"):
            emailanswer = str(input("Did you email? (Y/N)"))
            if emailanswer in ("Y", "y"):
                print(attemptlabel,
                      "Send email at email listed\n"
                      "Will make another attempt in 2 hours",
                      sep="\n")
                complete = True
            elif emailanswer in ("N", "n"):
                print("Complete")
                complete = True
            else:
                print("error")
        else:
            print("error")

    restart = str(input("Document another one? (Y/N) "))
