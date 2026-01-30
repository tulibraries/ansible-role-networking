import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


# Firewalld package should be installed
@pytest.mark.parametrize("pkg", ["firewalld"])
def test_firewalld_package_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


# Firewalld configuration files should exist
def test_firewalld_public_zone_config_exists(host):
    f = host.file("/etc/firewalld/zones/public.xml")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


# Firewalld rules are rendered into config (intent test)
@pytest.mark.parametrize("content", [
    '<service name="http"/>',
    '<service name="https"/>',
    '<port port="8080" protocol="tcp"/>',
])
def test_firewalld_public_zone_rules_rendered(host, content):
    f = host.file("/etc/firewalld/zones/public.xml")
    assert f.contains(content)
    
def test_firewalld_forward_port_not_rendered_when_disabled(host):
    f = host.file("/etc/firewalld/zones/public.xml")
    assert not f.contains('<forward-port port="80" protocol="tcp" to-port="8080"/>')
