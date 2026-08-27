from . import Expression

from sympy import Poly, solve_poly_inequality

# ============================================================================
# ================================ Inequation ================================
# ============================================================================

@Expression.register
class Inequation(Expression):
    """
    Inequation representation, solves any kind of inequality. Tested for the
    first and second degree.

    :warning: The inequation does not handle unknown-composed denominator as
    of 7 nov. 2017. A fix to the problem is currently being searched.
    """

    _db_type = "IN"

    # --------------------------------------------------------- Static methods

    @staticmethod
    def generate(two_sided, degree):
        raise NotImplementedError()

    # --------------------------------------------------------- Actual methods

    def resolve(self):
        """ return value of the solution of the inequation in a String"""
        results = []
        for sym in self._symbols:
            lfrac = self._getFrac(str(self._left_operand))
            rfrac = self._getFrac(str(self._right_operand))
            frac = lfrac + ['-'] + rfrac
            
            expr = self._unfraction(frac)
            den = self._getDenom(str(self._left_operand)+'-'+str(self._right_operand))

            polyExpr = Poly(expr, sym)
            if den!='' : polyDen = Poly(den, sym)
            else : polyDen = Poly('1', sym)

            posiCase = solve_poly_inequality(polyDen, '>')
            negaCase = solve_poly_inequality(polyDen, '<')
            posCase = posiCase[0]
            for cas in posiCase : posCase=posCase.union(cas)
            negCase = negaCase[0]
            for cas in negaCase : negCase=negCase.union(cas)
            
            posiSol = solve_poly_inequality( polyExpr, self._operator)
            negaSol = solve_poly_inequality(-polyExpr, self._operator)
            posSol = posiSol[0]
            for cas in posiSol : posSol=posSol.union(cas)
            negSol = negaSol[0]
            for cas in negaSol : negSol=negSol.union(cas)

                            
            result = (posCase.intersect(posSol)).union(negCase.intersect(negSol))
            results.append(result)
        return results

# ----------------------------------------------------------- Utility methods

    @staticmethod
    def _getFrac(expr):
        """ return the decomposed expression making difference
        between the numerator and the denominator"""
        expr=expr.replace(' ', '')
        l = len(expr)
        frac = []; start = 0; par = 0
        pack=''; num=''
        op = ['+','-']
        operator = ['+','-','/','*']
        sym = ['x','y']
        multFrac = False

        for i in range(0,l):
            if expr[i]=='(' :                               #(
                if par==0 : start=i
                par += 1
            elif expr[i] == ')' :                           #)
                par -= 1
                if par==0 :
                    pack += expr[start:i+1]; start = i+1
            elif expr[i]=='*'and par==0:                    #*
                pack += expr[start:i]; start = i+1
                if num!='' :
                    frac.append((num,pack))
                    frac.append(expr[i])
                    pack = ''; num = ''
                else :
                    pack += expr[i]
            elif expr[i]=='/'and par==0:                    #/
                pack += expr[start:i]
                num += pack
                pack = ''
                start = i+1
            elif expr[i] in op and par==0 and num != '':    #+-
                pack += expr[start:i]
                frac.append((num,pack))
                frac.append(expr[i])
                pack = ''; num = ''; start = i+1
            elif expr[i] in op and par==0:
                pack += expr[start:i]
                frac.append((pack,''))
                frac.append(expr[i])
                pack = ''; num = ''; start = i+1

        if start < l : pack += expr[start:l]
        if num != '' :
            frac.append((num,pack))
        else:
            frac.append((pack,''))

        frac2 = [frac[0]]
        i=1
        while i<len(frac):
            if frac[i] in operator and frac[i]!='*' :
                frac2.append(frac[i])
                frac2.append(frac[i+1])
            elif frac[i]=='*' :
                (a1,b1)=frac[i-1]
                (a2,b2)=frac[i+1]
                frac2[len(frac2)-1]=(a1+'*'+a2,b1+'*'+b2)
            i+=2
        return frac2
            
    @staticmethod
    def _unfraction(frac):
        """return the equation under the form of a multiplication of
        expression and without fractions"""
        expr = ''
        operator = ['+','-','/','*']

        for i in range(0,len(frac)):
            if frac[i] not in operator:
                expr += frac[i][0]
                for j in range(0,len(frac)):
                    if i != j and frac[j] not in operator and frac[j][1] != '':
                        expr += '*' + frac[j][1]
            else :
                expr += frac[i]
        return expr

    @staticmethod
    def _getDenom(expr):
        """ return the full denominator of the expression"""
        l = len(expr)
        den = ''
        i=0
        while i<l:
            if expr[i:i+2] == '/(' or expr[i:i+3] == '/ (':
                if den != '': den += '*'
                den += expr[i+1]
                par = 1
                i += 2
                while par > 0:
                    if expr[i] == '(': par += 1
                    elif expr[i] == ')': par -= 1
                    den += expr[i]
                    i += 1
            else :i += 1
        return den

# ============================================================================
