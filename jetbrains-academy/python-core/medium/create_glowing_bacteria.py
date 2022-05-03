def create_complementary_strand(origin):
    complementarity = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complementarity.get(p) for p in origin)


def cut_plasmid_sequence(origin, complementary, restriction_site):
    pos = origin.find(restriction_site)
    return [(origin[:(pos + 1)], origin[(pos + 1):]), (complementary[:(pos + 5)], complementary[(pos + 5):])]


def cut_gfp_sequence(origin, complementary, rs_left, rs_right):
    pos_left = origin.find(rs_left)
    pos_right = origin.rfind(rs_right)
    return [origin[(pos_left + 1):(pos_right + 1)], complementary[(pos_left + 5):(pos_right + 5)]]


with open(input()) as f:
    raw = f.read().splitlines()
    plasmid_origin, plasmid_restriction_site, gfp_origin = raw[0], raw[1], raw[2]
    gfp_rs_left, gfp_rs_right = raw[3].split()

plasmid_complementary = create_complementary_strand(plasmid_origin)
plasmid_cut = cut_plasmid_sequence(plasmid_origin, plasmid_complementary, plasmid_restriction_site)
gfp_complementary = create_complementary_strand(gfp_origin)
gfp_cut = cut_gfp_sequence(gfp_origin, gfp_complementary, gfp_rs_left, gfp_rs_right)

print(f'{plasmid_cut[0][0]}{gfp_cut[0]}{plasmid_cut[0][1]}')
print(f'{plasmid_cut[1][0]}{gfp_cut[1]}{plasmid_cut[1][1]}')
