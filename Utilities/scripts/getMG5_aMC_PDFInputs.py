from PDFSetsChooserTools import PDFSetHelper_MG5_aMC
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', choices=['systematics', 'central', 'members', 'sets'], 
        required=True, help='Output PDF set list or list of members to store')
parser.add_argument('-c', '--pdf_choice', choices=['custom', 'campaign', '2016', '2017'],
        required=True, help="Use 2017 or 2016 defaults or custom choice")
parser.add_argument('--is5FlavorScheme', action='store_true',
        help='Use PDF set for 5 flavor scheme (vs. 4F if false)')
parser.add_argument('--isNLO', action='store_true',
        help='NLO vs. LO MG5_aMC@NLO')
parser.add_argument('--pdf_path', action='store',
        help='path to PDF directory')

args = parser.parse_args()

helper = PDFSetHelper_MG5_aMC()
if args.pdf_choice == '2017':
    helper.readDefaultPDFsFile(args.is5FlavorScheme)
elif args.pdf_choice == "campaign":
    helper.readCampaignPDFsFile(args.is5FlavorScheme, args.pdf_path)
else:
    #TODO Implement option for custom PDF list
    print "Custom sets not yet supported!"
    exit(1)

if args.format == "central":
    print helper.getListOfLHAPDFIds(False)
    exit(0)
elif args.format == "sets":
    print helper.getListOfLHAPDFIds(args.isNLO)
    exit(0)
elif args.format == "members":
    # Only used for NLO 
    print helper.getListOfMembersToStore()
    exit(0)
# Format pdf list for systematics program
# See https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Systematics
elif args.format == "systematics":
    print helper.getListOfLHAPDFIdsForSystematics()
    exit(0)

