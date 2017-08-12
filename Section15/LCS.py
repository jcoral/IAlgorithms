# -*- coding: utf-8 -*-

def makeRange(ai, bi, splitChr = "-"):
    """
    根据开始的位置和结束的位置返回一个范围字符串
    :param start: 开始的位置
    :param end:   结束的位置
    :return:      str
    """
    return str(ai) + splitChr + str(bi)

bp = {}

def calLCS(A, B, ai = 0, bi = 0):
    """
    下标1开始
    思想：设A的长度为m，B的长度为n， 给定不等式 1 <= ai <= m, 1 <= bi <= n
         在A中找到所有使得与B[bi]同的值， 然后计算max(|A[ai] + calLCS(ai + 1, bi + 1)|)

    例如:
    下标从1开始
    设A = ACCGGTCG， B = GTCGTTCG
    遍历序列B
    当bi = 1时，对齐到A时ai = 4，此时则求A子序列GTCG作为A1和B子序列TCGTTCG作为B1的最长子序列
        求A1和B1的最长子序列
        当bi = 1时，对齐到A1时ai = 2， 此时则求A1子序列CG作为A11和B1子序列CGTTCG作为B11的最长子序列
            求A11和B11的最长子序列
            当bi = 1时，对齐到A11时ai = 1，此时则求A11子序列G作为B111和B11子序列GTTCG作为B111的最长子序列
                求A111和B111的最长子序列
                当bi = 1时， 对齐到A111时ai = 1， 此时最长子序列为G
            A11和B11的最长子序列为CG
        A1和B1的最长子序列为TCG
    当bi = 1时，A和B的最长子序列为GTCG

    当bi = 2时， 与步骤bi = 1时类似

    :param A: 序列1
    :param B: 序列2
    :param ai: A的开始位置
    :param bi: B的开始位置
    :return:   LCS
    """
    op = []
    for bindex in range(bi, len(B)):
        for aindex in range(ai, len(A)):
            if A[aindex] == B[bindex]:
                if bp.__contains__(makeRange(aindex + 1, bindex + 1)):
                    subs = bp[makeRange(aindex + 1, bindex + 1)]
                else:
                    subs = calLCS(A, B, aindex + 1, bindex + 1)

                if len(op) < len([A[aindex]] + subs):
                    op = [A[aindex]] + subs

                break
    bp[makeRange(ai, bi)] = op
    return op

if __name__ == '__main__':
    A = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    B = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    print "".join(calLCS(A, B))











