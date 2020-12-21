import rhinoscriptsyntax as rs


idSrf = rs.GetObject("surface to frame", 8, True, True)
intCountU = rs.GetInteger("Number of iterations in U direction", 10, 1)
intCountV = rs.GetInteger("Number of iterations in V direction", 10, 1)

def srfLoft(idCrv_i,idCrv_ii):
    idPlLine = idCrv_i
    coordPlLine = rs.CurveStartPoint(idPlLine)
    rs.AddPoint(coordPlLine)
    idCrv = idCrv_ii
    coordCrv = rs.CurveStartPoint(idCrv)
    listCrvs = [idPlLine,idCrv]
    param = rs.CurveClosestPoint(idPlLine,coordCrv)
    rs.CurveSeam(idPlLine,param)
    rs.AddLoftSrf(listCrvs,None,None,0,0,0,False)

def Func_4(idSrf,Matrix, intCountU,intCountV):
    k = 0
    for u in range (0,intCountU):
        if (u % 2 != 0) :
            k = 1
        else:
            k = 0
        for v in range (0, intCountV):
            Pt0 = Matrix[u][v]
            Pt1 = Matrix[u+1][v]
            Pt2 = Matrix[u+1][v+1]
            Pt3 = Matrix[u][v+1]
            points_L = [Pt3,Pt2,Pt1,Pt0]
            points_R = [Pt0,Pt1,Pt2,Pt3]
            #--------------------------------------------
            idSrf_internal_L = rs.AddSrfPt(points_L)
            idSrf_internal_R = rs.AddSrfPt(points_R)
            
            uDomain_internal = rs.SurfaceDomain(idSrf_internal_L, 0)
            vDomain_internal = rs.SurfaceDomain(idSrf_internal_L, 1)
            uStep_internal = (uDomain_internal[1] - uDomain_internal[0]) / 2
            vStep_internal = (vDomain_internal[1] - vDomain_internal[0]) / 2
            param = [uStep_internal,vStep_internal]
            centerPoint = rs.SurfaceAreaCentroid(idSrf_internal_L)
            
            normal_L = rs.SurfaceNormal (idSrf_internal_L, param)
            normal_R = rs.SurfaceNormal (idSrf_internal_R, param)
            
            LineNormSmall_L = rs.AddLine (centerPoint[0] ,rs.VectorAdd(centerPoint[0], normal_L) )
            LineNormSmall_R = rs.AddLine (centerPoint[0] ,rs.VectorAdd(centerPoint[0], normal_R) )
            
            LineNormBig_L = rs.ExtendCurveLength (LineNormSmall_L, 0,2,  2)
            LineNormBig_R = rs.ExtendCurveLength (LineNormSmall_R, 0,2,  2)
            
            NrmlPoint_L = rs.CurveEndPoint(LineNormBig_L)
            NrmlPoint_R = rs.CurveEndPoint(LineNormBig_R)
            #--------------------------------------------
            if k == 0:
                idCrv_i     = rs.AddCurve([Pt0,NrmlPoint_L,Pt1],3)
                idCrv_ii    = rs.AddCurve([Pt3,NrmlPoint_L,Pt2],3)
                idCrv_iii   = rs.AddCurve([Pt0,NrmlPoint_R,Pt3],3)
                idCrv_iv    = rs.AddCurve([Pt1,NrmlPoint_R,Pt2],3)
                
                srfLoft(idCrv_i,idCrv_ii)
                srfLoft(idCrv_iii,idCrv_iv)
                k=1
            else:
                idCrv_i     = rs.AddCurve([Pt0,NrmlPoint_L,Pt1],3)
                idCrv_ii    = rs.AddCurve([Pt3,NrmlPoint_L,Pt2],3)
                idCrv_iii   = rs.AddCurve([Pt0,NrmlPoint_R,Pt3],3)
                idCrv_iv    = rs.AddCurve([Pt1,NrmlPoint_R,Pt2],3)
                
                srfLoft(idCrv_i,idCrv_ii)
                srfLoft(idCrv_iii,idCrv_iv)
                k=0
            rs.DeleteObject(idSrf_internal_L)
            rs.DeleteObject(idSrf_internal_R)
            rs.DeleteObject(LineNormSmall_L)
            rs.DeleteObject(LineNormSmall_R)


def SurfaceEvaluateDivide(idSrf, intCountU, intCountV):
    uDomain = rs.SurfaceDomain(idSrf, 0)
    vDomain = rs.SurfaceDomain(idSrf, 1)
    uStep = (uDomain[1] - uDomain[0]) / intCountU
    vStep = (vDomain[1] - vDomain[0]) / intCountV
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
Func_4(idSrf, Matrix_uv, intCountU, intCountV)
rs.EnableRedraw(True)