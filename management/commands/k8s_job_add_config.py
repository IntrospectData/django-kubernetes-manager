import hashlib
from argparse import ArgumentParser, FileType
from io import StringIO
from sys import stdin, stdout

import yaml
from django.core.management import call_command
from django.core.management.base import BaseCommand

from k8s_job.models import TargetCluster


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("kubeconfig", nargs="?", type=FileType("r"), default=stdin)

    def handle(self, *args, **options):
        input = options["kubeconfig"]
        input_txt = input.read()
        TargetCluster.add(input_txt)
