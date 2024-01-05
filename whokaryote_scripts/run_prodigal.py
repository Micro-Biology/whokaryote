""" Run gene prediction with prodigal, metagenomics mode. """

import subprocess
import os


def run_prodigal(contig_file, outdir, threads):
    genes_output = os.path.join(outdir, "contigs_genes.gff")
    proteins_output = os.path.join(outdir, "contigs_proteins.faa")
    print(f"    pprodigal using {threads} threads and splitting into 2000 sequences per chunk")
    subprocess.call(
        ["pprodigal", "-i", contig_file, "-o", genes_output, "-a", proteins_output, "-p", "meta", "-f", "gff", "-q", "-T", threads])
