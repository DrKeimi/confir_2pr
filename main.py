import sys
import requests
import json
import graphviz


def fetch_dependencies(repo_url):
    new_url = repo_url.replace('github.com', 'raw.githubusercontent.com')
    npm_url = f"{new_url}/refs/heads/main/package.json"
    response = requests.get(npm_url)
    print(npm_url)
    package_data = response.json()

    dependencies = package_data.get('dependencies', {})
    if len(dependencies) == 0:
        dependencies = package_data.get('devDependencies', {})
    return dependencies


def build_graph(dependencies, graph, parent=None):
    for dep, version in dependencies.items():
        graph.node(dep)

        graph.edge(parent, dep)



def visualize_graph(package_name, repo_url):
    dependencies = fetch_dependencies(repo_url)
    graph = graphviz.Digraph(comment='Dependency Graph')

    graph.node(package_name)
    build_graph(dependencies, graph, package_name)

    graph.render(f'{package_name}', format='png', cleanup=True)



if __name__ == "__main__":
    path_to_graphviz = sys.argv[1]
    package_name = sys.argv[2]
    repo_url = sys.argv[3]

    visualize_graph(package_name, repo_url)

