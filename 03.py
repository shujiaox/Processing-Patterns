import rhinoscriptsyntax as rs
import math 


idSrf = rs.GetObject("surface to frame", 8, True, True)
intCountU = rs.GetInteger("Number of iterations in U direction", 20, 1)
intCountV = rs.GetInteger("Number of iterations in V direction", 20, 1)

def srfLoft(idCrv_i,idCrv_ii):
    idPlLine = idCrv_i
    coordPlLine = rs.CurveStartPoint(idPlLine)
    rs.AddPoint(coordPlLine)
    idCrv = idCrv_ii
    coordCrv = rs.CurveStartPoint(idCrv)
    listCrvs = [idPlLine,idCrv]
    param = rs.CurveClosestPoint(idPlLine,coordCrv)
    rs.CurveSeam(idPlLine,param)
    rs.AddPoint(coordCrv)
    rs.AddLoftSrf(listCrvs,None,None,0,0,0,False)
def Func_2(idSrf, Matrix, intCountU, intCountV):
    for u in range(0,intCountU):
        if u % 2 != 0 :
            k = 1
        else:
            k = 0
        for v in range(0,intCountV):
            Pt0 = Matrix[u][v]
            Pt1 = Matrix[u+1][v]
            Pt2 = Matrix[u+1][v+1]
            Pt3 = Matrix[u][v+1]
            listPoints = [Pt0,Pt1,Pt2,Pt3,Pt0]
            idPlLine = rs.AddPolyline(listPoints)
            if k ==0 :
                listPointCrv1_p1= [Pt0, Pt1, Pt2]
                listPointCrv1_p2= [Pt0, Pt3, Pt2]
                idCrv_1_p1 = rs.AddCurve(listPointCrv1_p1)
                idCrv_1_p2 = rs.AddCurve(listPointCrv1_p2)
                idCrv_1 = rs.JoinCurves([idCrv_1_p1,idCrv_1_p2],True)
                srfLoft(idPlLine,idCrv_1[0])
                k = 1
            else:
                listPointCrv1_p1= [Pt0, Pt1, Pt2]
                listPointCrv1_p2= [Pt0, Pt3, Pt2]
                idCrv_1_p1 = rs.AddCurve(listPointCrv1_p1)
                idCrv_1_p2 = rs.AddCurve(listPointCrv1_p2)
                idCrv_1 = rs.JoinCurves([idCrv_1_p1,idCrv_1_p2],True)
                srfLoft(idPlLine,idCrv_1[0])
                k = 0
def SurfaceEvaluateDivide(idSrf, intCountU, intCountV):
    uDomain = rs.SurfaceDomain(idSrf, 0)
    vDomain = rs.SurfaceDomain(idSrf, 1)
    uStep = math.fabs (uDomain[1] - uDomain[0]) / intCountU
    vStep = math.fabs (vDomain[1] - vDomain[0]) / intCountV
    Matrix_uv = []

    for u in rs.frange (uDomain[0], uDomain[1], uStep):
        Matrix_v = []
        for v in rs.frange (vDomain[0], vDomain[1], vStep):
            pt = rs.EvaluateSurface(idSrf,u,v)
            Matrix_v.append(pt)
        Matrix_uv.append(Matrix_v)
    return Matrix_uv
rs.EnableRedraw(False)
Matrix_uv = SurfaceEvaluateDivide(idSrf,intCountU,intCountV)
Func_2(idSrf, Matrix_uv, intCountU, intCountV)
rs.EnableRedraw(True)