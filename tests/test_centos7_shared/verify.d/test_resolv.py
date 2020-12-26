def test_resolv_containt_two_entires(host):
    assert host.check_output("grep ^nameserver /etc/resolv.conf |wc -l") == "2"
