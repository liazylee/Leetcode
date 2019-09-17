'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

class  Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in xrange(0,len(nums)):

                dic[nums[i]]=i
        try:

            item=dic[nums[i]]
            item2=dic[target-nums[i]]
            if item>item2 and dic[item2] !=dic[item]:
                l=[item2,item]
            elif item<item2 and dic[item2] !=dic[item]:
                l=[item,item2]
            return l

        except:
            pass
    def Twosum(self,nums,target):
        lookup = dict(((v, i) for i, v in enumerate(nums)))
        return next(((i , lookup.get(target - v))
                     for i, v in enumerate(nums)
                     if lookup.get(target - v, i) != i), None)
    # def twosum(self,nums,target):
    #     lookup=dict((v,i)for i,v in enumerate(nums))
    #     for i, v in lookup:
    #         if lookup.get(target-v,i) !=i


if __name__=='__main__':
    a=Solution()
    print a.twoSum([1,3,4],7)
    """
    {
	"configs" : [
		{
			"remarks" : "",
			"id" : "1E83B19017728529AE26665AE9D585AF",
			"server" : "104.225.147.9",
			"server_port" : 8811,
			"server_udp_port" : 0,
			"password" : "li1314",
			"method" : "aes-256-cfb",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "",
			"group" : "FreeSSR-public",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "洛杉矶E",
			"id" : "23101529F8B5E93A0D0E43D4C138D297",
			"server" : "139.28.235.117",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 8k",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5rSb5p2J55-2RQ",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "莫斯科C",
			"id" : "8683F18E68C7EACFE7A8A57EC05664C0",
			"server" : "45.129.2.172",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 6j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "6I6r5pav56eRQw",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "莫斯科B",
			"id" : "E75AB7AED993DEC71A6C50EDE0338504",
			"server" : "45.129.2.170",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 6j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "6I6r5pav56eRQg",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "莫斯科A",
			"id" : "EBD03E18543A3A128B111E76540C4045",
			"server" : "45.129.2.171",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 6j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "6I6r5pav56eRQQ",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "东京Y",
			"id" : "9FDBD846BDE982A502B825212FC180B7",
			"server" : "193.38.139.232",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 7j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5Lic5LqsWQ",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "东京X",
			"id" : "A2E66A9DCDC3B53CE8ECCFC0A15ED76E",
			"server" : "194.156.230.114",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 7j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5Lic5LqsWA",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "东京F",
			"id" : "C552E273E516E57F13884E4D1A495562",
			"server" : "45.12.207.105",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 7j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5Lic5LqsRg",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "东京E",
			"id" : "D0D0C7F4E5938DBB672E444F38D78C9A",
			"server" : "45.12.207.104",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 7j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5Lic5LqsRQ",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "东京D",
			"id" : "1A677761E78DF6F0BCB36CA45D422EE3",
			"server" : "5.180.77.47",
			"server_port" : 3389,
			"server_udp_port" : 0,
			"password" : "lncn.org 6j",
			"method" : "rc4",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "5Lic5LqsRA",
			"group" : "@1024",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "",
			"id" : "8BF9CF4D8C7A9DAD15CA82422C5C17AB",
			"server" : "66.112.218.12",
			"server_port" : 7790,
			"server_udp_port" : 0,
			"password" : "tanzuji",
			"method" : "aes-256-cfb",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "",
			"group" : "FreeSSR-public",
			"enable" : true,
			"udp_over_tcp" : false
		},
		{
			"remarks" : "",
			"id" : "34DB3B0EC06720A8E07259240DB1D21B",
			"server" : "66.112.218.12",
			"server_port" : 7789,
			"server_udp_port" : 0,
			"password" : "tanzuji",
			"method" : "aes-256-cfb",
			"protocol" : "origin",
			"protocolparam" : "",
			"obfs" : "plain",
			"obfsparam" : "",
			"remarks_base64" : "",
			"group" : "FreeSSR-public",
			"enable" : true,
			"udp_over_tcp" : false
		}
	],
	"index" : 0,
	"random" : true,
	"sysProxyMode" : 3,
	"shareOverLan" : false,
	"localPort" : 1080,
	"localAuthPassword" : "4alizeYEjVejqpf-kdSY",
	"dnsServer" : "",
	"reconnectTimes" : 2,
	"randomAlgorithm" : 3,
	"randomInGroup" : false,
	"TTL" : 0,
	"connectTimeout" : 5,
	"proxyRuleMode" : 2,
	"proxyEnable" : false,
	"pacDirectGoProxy" : false,
	"proxyType" : 0,
	"proxyHost" : null,
	"proxyPort" : 0,
	"proxyAuthUser" : null,
	"proxyAuthPass" : null,
	"proxyUserAgent" : null,
	"authUser" : null,
	"authPass" : null,
	"autoBan" : false,
	"sameHostForSameTarget" : false,
	"keepVisitTime" : 180,
	"isHideTips" : false,
	"nodeFeedAutoUpdate" : true,
	"serverSubscribes" : [

	],
	"token" : {

	},
	"portMap" : {

	}
}"""
