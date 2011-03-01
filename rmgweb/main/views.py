from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import django.contrib.auth.views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forms import UserProfileForm

def index(request):
    """
    The RMG website homepage.
    """
    return render_to_response('index.html', context_instance=RequestContext(request))

def login(request):
    """
    Called when the user wishes to log in to his/her account.
    """
    return django.contrib.auth.views.login(request, template_name='login.html')

def logout(request):
    """
    Called when the user wishes to log out of his/her account.
    """
    return django.contrib.auth.views.logout(request, template_name='logout.html')

def viewProfile(request, username):
    """
    Called when the user wishes to view another user's profile. The other user
    is identified by his/her `username`. Note that viewing user profiles does
    not require authentication.
    """
    user0 = User.objects.get(username=username)
    return render_to_response('viewProfile.html', {'user0': user0}, context_instance=RequestContext(request))

@login_required
def editProfile(request):
    """
    Called when the user wishes to edit his/her user profile.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = UserProfileForm(instance=request.user) # An unbound form

    return render_to_response('editProfile.html', {'form': form}, context_instance=RequestContext(request))

def drawMolecule(request, adjlist):
    """
    Returns an image of the provided adjacency list `adjlist` for a molecule.
    Note that the newline character cannot be represented in a URL;
    semicolons should be used instead.
    """
    from rmgpy.chem.molecule import Molecule
    from rmgpy.chem.ext.molecule_draw import drawMolecule

    response = HttpResponse(mimetype="image/png")

    adjlist = str(adjlist.replace(';', '\n'))
    molecule = Molecule().fromAdjacencyList(adjlist)
    surface, cr, rect = drawMolecule(molecule, surface='png')
    surface.write_to_png(response)

    return response

def drawMoleculePattern(request, adjlist):
    """
    Returns an image of the provided adjacency list `adjlist` for a molecular
    pattern. Note that the newline character cannot be represented in a URL;
    semicolons should be used instead.
    """
    from rmgpy.chem.pattern import MoleculePattern
    import pydot

    response = HttpResponse(mimetype="image/png")

    adjlist = str(adjlist.replace(';', '\n'))
    pattern = MoleculePattern().fromAdjacencyList(adjlist)

    graph = pydot.Dot(graph_type='graph', dpi=75)
    for index, atom in enumerate(pattern.atoms):
        atomType = '%s ' % atom.label if atom.label != '' else ''
        atomType += ','.join([atomType.label for atomType in atom.atomType])
        graph.add_node(pydot.Node(name='%i' % (index+1), label=atomType, fontname='sans', fontsize=12))
    for atom1, bonds in pattern.bonds.iteritems():
        for atom2, bond in bonds.iteritems():
            index1 = pattern.atoms.index(atom1)
            index2 = pattern.atoms.index(atom2)
            if index1 < index2:
                bondType = ','.join([order for order in bond.order])
                graph.add_edge(pydot.Edge(
                    src = '%i' % (index1+1),
                    dst = '%i' % (index2+1),
                    label = bondType,
                    fontname='sans', fontsize = 12,
                ))

    response.write(graph.create(prog='neato', format='png'))

    return response
