import pysam

samfile = pysam.AlignmentFile("/Users/sandert/Desktop/sorted.bam", "rb")
for pileupcolumn in samfile.pileup("NC_045512.2", 21985, 21989):
    if pileupcolumn.pos in [21986]:

        for pileupread in pileupcolumn.pileups:
            if not pileupread.is_del and not pileupread.is_refskip:
                # query position is None if is_del or is_refskip is set.
                print(
                    pileupcolumn.pos,
                    pileupread.alignment.query_sequence[
                        pileupread.query_position],
                    pileupread.alignment.reference_start,
                    pileupread.alignment.reference_end,
                )

samfile.close()