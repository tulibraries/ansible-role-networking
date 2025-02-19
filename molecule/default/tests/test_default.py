import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


# Firewalld Exists
@pytest.mark.parametrize('pkg', ['firewalld'])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


# Firewalld is Running
@pytest.mark.parametrize('svc', ['firewalld'])
def test_svc(host, svc):
    service = host.service(svc)
    assert service.is_running
    assert service.is_enabled


# Firewall rules for Public Zone and Enabled Status are present
@pytest.mark.parametrize('file, content', [
    ("/etc/firewalld/zones/public.xml", "<service name=\"http\"/>"),
    ("/etc/firewalld/zones/public.xml", "<service name=\"https\"/>"),
    ("/etc/firewalld/zones/public.xml",
     "<port port=\"8080\" protocol=\"tcp\"/>"),
    ("/etc/firewalld/zones/public.xml",
     "<forward-port port=\"80\" protocol=\"tcp\" to-port=\"8080\"/>")
    ])
def test_public_services(host, file, content):
    file = host.file(file)
    assert file.exists
    assert file.contains(content)
