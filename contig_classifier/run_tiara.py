""" Run gene prediction with prodigal, metagenomics mode. """

import subprocess
import os


def run_tiara(contig_file, outdir):
    prediction_output = os.path.join(outdir, "tiara_pred.txt")
    proteins_output = os.path.join(outdir, "contigs_proteins.faa")

    subprocess.call(
        ["tiara", "-i", contig_file, "-o", prediction_output, "-m 3000"])
