from urllib2 import Request, urlopen 

from urllib import urlencode, quote_plus 

url = 'https://api-na.hosted.exlibrisgroup.com/almaws/v1/conf/jobs/{job_id}'.replace('{job_id}',quote_plus('M47')) 

queryParams = '?' + urlencode({ quote_plus('op') : 'run' ,quote_plus('apikey') : 'your-key' }) 

values = \
"""<job>
	<parameters>
		<parameter>
			<name>task_ExportBibParams_outputFormat_string</name>
			<value>GOOGLE_SCHOLAR</value>
		</parameter>
		<parameter>
			<name>task_ExportBibParams_maxSize_string</name>
			<value>0</value>
		</parameter>
		<parameter>
			<name>task_ExportBibParams_exportFolder_string</name>
			<value>PRIVATE</value>
		</parameter>
		<parameter>
			<name>task_ExportParams_ftpConfig_string</name>
			<value>11899028490002766</value>
		</parameter>
		<parameter>
			<name>task_ExportParams_ftpSubdirectory_string</name>
			<value></value>
		</parameter>
		<parameter>
			<name>task_ExportParams_interfaceName</name>
			<value>true</value>
		</parameter>
		<parameter>
			<name>task_ExportParams_filterInactivePortfolios</name>
			<value>false</value>
		</parameter>
		<parameter>
			<name>task_ExportParams_baseUrl</name>
			<value/>
		</parameter>
		<parameter>
			<name>set_id</name>
			<value>11050905180002766</value>
		</parameter>
		<parameter>
			<name>job_name</name>
			<value>Export Electronic Portfolios - via API - jeb etitle journals for Main access (&amp; free)</value>
		</parameter>
	</parameters>
</job>""" 

headers = { 'Content-Type':'application/xml' } 

request = Request(url + queryParams 
, data=values 
, headers=headers) 

request.get_method = lambda: 'POST' 

response_body = urlopen(request).read() 

print response_body
