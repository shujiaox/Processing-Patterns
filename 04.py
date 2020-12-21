
import rhinoscriptsyntax as rs
import math 


Srf = rs.GetObject("surface to frame", 8, True, True)


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

def Func_3(Srf, Matrix):
    for u in range(0,10):
        for v in range(0,10):
            p0 = Matrix[u][v]
            p1 = Matrix[u+1][v]
            p2 = Matrix[u+1][v+1]
            p3 = Matrix[u][v+1]
            listPoints = [p0,p1,p2,p3,p0]
            idCrv = rs.AddCurve(listPoints)
            idPlLine = rs.AddPolyline(listPoints) 
            coorCenterPoint = (p0+p1+p2+p3)/4
            #coorCenterPoint = rs.CurveAreaCentroid(idCrv)
            cs = rs.SurfaceClosestPoint(Srf, coorCenterPoint)
            normal = rs.SurfaceNormal(Srf,cs)
            scale = rs.Distance(p0,p1)
            normal = rs.VectorScale(normal,scale/((u+v)/10+0.1))
            normal = rs.VectorAdd(coorCenterPoint,normal)
            rs.AddLine(coorCenterPoint,normal)
            #centerPoint = rs.AddPoint(normal)
            translation = rs.VectorSubtract(normal,coorCenterPoint)
            idCrv = rs.MoveObject(idCrv,translation)
            srfLoft(idPlLine,idCrv)

def Tesselation(Srf):
    uDomain = rs.SurfaceDomain(Srf, 0)
    vDomain = rs.SurfaceDomain(Srf, 1)
    uStep = math.fabs (uDomain[1] - uDomain[0]) / 10
    vStep = math.fabs (vDomain[1] - vDomain[0]) / 10
    Matrix_uv = []

    for u in rs.frange (uDomain[0], uDomain[1], uStep):
        Matrix_v = []
        for v in rs.frange (vDomain[0], vDomain[1], vStep):
            pt = rs.EvaluateSurface(Srf,u,v)
            Matrix_v.append(pt)
        Matrix_uv.append(Matrix_v)
    return Matrix_uv
rs.EnableRedraw(False)
Matrix_uv = Tesselation(Srf)
Func_3(Srf, Matrix_uv)
rs.EnableRedraw(True)