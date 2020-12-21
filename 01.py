import rhinoscriptsyntax as rs
import math 


idSrf = rs.GetObject("surface to frame", 8, True, True)
intCountU = rs.GetInteger("Number of iterations in U direction", 5, 1)
intCountV = rs.GetInteger("Number of iterations in V direction", 5, 1)

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

def StarSrf(Matrix, intCountU, intCountV):
    rs.EnableRedraw(False)
    for u in range(0,intCountU):
        for v in range(0,intCountV):
            Pt0 = Matrix[u][v]
            Pt1 = Matrix[u+1][v]
            Pt2 = Matrix[u+1][v+1]
            Pt3 = Matrix[u][v+1]
            points = [Pt0,Pt1,Pt2,Pt3]
            tempSrf = rs.AddSrfPt(points)
            centerPoint = rs.SurfaceAreaCentroid(tempSrf)
            rs.DeleteObject(tempSrf)
            idCrv0 = rs.AddCurve([Pt0,centerPoint[0],Pt1])
            idCrv1 = rs.AddCurve([Pt1,centerPoint[0],Pt2])
            idCrv2 = rs.AddCurve([Pt2,centerPoint[0],Pt3])
            idCrv3 = rs.AddCurve([Pt3,centerPoint[0],Pt0])
            idStarSrf = rs.AddEdgeSrf([idCrv0,idCrv1,idCrv2,idCrv3])
            coorCenterPoint = rs.SurfaceAreaCentroid(idStarSrf)
            normal = rs.SurfaceNormal(idSrf,[u,v])
            scale = rs.Distance(Pt0,Pt1)
            normal = rs.VectorScale(normal,scale*10)
            normal = rs.VectorAdd(normal,coorCenterPoint[0])
            centerPoint = rs.AddPoint(normal)
            rs.UnselectAllObjects()
            listPatch = [idCrv0,idCrv1,idCrv2,idCrv3,centerPoint]
            rs.SelectObjects(listPatch)
            rs.Command(" _-Patch" + " _enter ")
            rs.DeleteObject(centerPoint)
            
    rs.DeleteObject(idSrf)
    rs.EnableRedraw(True)

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
StarSrf( Matrix_uv, intCountU, intCountV)
rs.EnableRedraw(True)