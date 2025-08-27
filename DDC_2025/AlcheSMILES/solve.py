MOLECULE_DB = [
"C","CC","CCC","O","CO","CCO","N","CN","CCN","S","CS","CCS","F","CF","CCF","Cl","CCl","CCCl","Br","CBr","HOH","OO","OCO",
"c1ccccc1","Cc1ccccc1","OCc1ccccc1","Nc1ccccc1","Sc1ccccc1","c1ccc(C)cc1","c1ccc(O)cc1","c1ccc(N)cc1","c1ccc(S)cc1",
"c1ccc(F)cc1","CC(C)C","CC(C)O","CC(C)N","CC(C)S","CC(C)F","CCCC","CCCCO","CCCCN","CCCCS","CCCCF","C1CC1","C1CCO1","C1CCN1","C1CCS1","C1CCF1",
"C=C","C=CO","C=CN","C=CS","C=CF","C#C","C#CO","C#CN","C#CS","C#CF","c1ccncc1","c1ccnc(C)c1","c1ccnc(O)c1","c1ccnc(N)c1","c1ccnc(S)c1",
"CC=C","CCC=C","CCCC=C","CCCCC=C","CCCCCC=C","c1cccnc1","c1ccc(C=C)cc1","c1ccc(C#C)cc1","c1ccc(CC)cc1","c1ccc(CCC)cc1",
"COC","CCOC","CCCOC","CCCCOC","CCCCCOC","CNC","CCNC","CCCNC","CCCCNC","CCCCCNC","CSC","CCSC","CCCSC","CCCCSC","CCCCCSC",
"CFC","CCFC","CCCFC","CCCCFC","CCCCCFC","ClCCl","BrCBr","ICl","ClF","BrF","c1ccc2ccccc2c1","c1ccc2cc(C)ccc2c1","c1ccc2cc(O)ccc2c1","c1ccc2cc(N)ccc2c1","c1ccc2cc(S)ccc2c1",
"CC(C)(C)C","CC(C)(C)O","CC(C)(C)N","CC(C)(C)S","CC(C)(C)F","C1CCC1","C1CCCO1","C1CCCN1","C1CCCS1","C1CCCF1","C1CCCC1","C1CCCCO1","C1CCCCN1","C1CCCCS1","C1CCCCF1",
"C1CCCCC1","C1CCCCCO1","C1CCCCCN1","C1CCCCCS1","C1CCCCCF1","c1ccc(C(C)C)cc1","c1ccc(C(C)O)cc1","c1ccc(C(C)N)cc1","CC(=O)C","CC(=O)O"
]

ENCODED = ("CCCC.CCCC.CC(C)F.C.HOH.c1ccc(S)cc1.CCOC.C1CCCC1.CC(C)S.Cc1ccccc1.CC(=O)C.c1ccc(S)cc1.C1CCCC1.c1ccc(S)cc1."
           "BrCBr.CC(C)S.C1CCCCCS1.C1CCCO1.c1ccc(S)cc1.C=CF.c1ccc(C#C)cc1.CC(C)(C)N.C1CCCC1.CCOC.c1ccc(C#C)cc1.c1ccc(CC)"
           "cc1.c1ccc(S)cc1.BrF.OCc1ccccc1.c1ccc(S)cc1.C=CF.c1ccc(C#C)cc1.HOH.Cc1ccccc1.c1ccc(S)cc1.CCCCS.c1ccc(C#C)cc1."
           "CC(C)S.C1CCO1.HOH.Cc1ccccc1.c1ccc(CC)cc1.CF.Nc1ccccc1.c1ccc(S)cc1.CC(C)S.BrCBr.CCCCS.CF.Nc1ccccc1.N.c1ccc(CC)"
           "cc1.HOH.CC(C)(C)N.BrCBr.OO")
list_string = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
list_string_enc = "BrF.HOH.CC(=O)O.CC(C)S.C1CCCO1.CC(=O)C.c1ccnc(C)c1.C=CF.CSC.C#CS.CCC.O.CCCCS.ClCCl.C=CS.OCc1ccccc1.CCOC.c1ccc(C#C)cc1.CCCl.c1ccc(C(C)N)cc1.C1CCCF1.CCSC.C1CCO1.BrCBr.CC(C)(C)N.N.CCCCF.CF.Cc1ccccc1.c1ccc(CC)cc1.C1CCCC1.C1CCCCCS1.CCNC.Cl.Nc1ccccc1.C1CCCCCO1.CC.CN.CC(C)F.CCCC.c1ccc(C)cc1.CC(C)N.C#C.CCCC=C.CCN.C1CCF1.S.C1CCCCS1.C=C.Br.CBr.CC=C.CCS.C1CCN1.Sc1ccccc1.C1CCCCCF1.C1CCC1.c1ccc2cc(O)ccc2c1.c1ccnc(S)c1.F.c1ccc2cc(N)ccc2c1.CC(C)(C)F.CCCCSC.c1ccc(C=C)cc1.C1CCCCN1.C#CO.c1ccc2ccccc2c1.ICl.ClF.CC(C)(C)O.CCO.CCCFC.C1CCC N1.c1ccccc1.C1CCCS1.CCFC.CCCCCOC.COC.OCO.CC(C)(C)C.CCC=C.C1CCCCF1.CCl.CCCCCFC.C=CN.CC(C)C.CCCCCNC.CS.c1ccc(S)cc1.CCCCC=C.C.c1ccc(N)cc1.OO.c1ccc(C(C)C)cc1"
list_string_enc = list_string_enc.split(".")
ENCODED = ENCODED.split(".")
for i in range(len(ENCODED)):
    for j in range(len(list_string_enc)):
        if ENCODED[i] == list_string_enc[j]:
           print(list_string[j], end="")

# DDC{1_gu3s5_u_n3v4_7hought_0f_7h1s_ch3m1stry_3ncrypt1on}