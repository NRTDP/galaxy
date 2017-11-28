<%inherit file="/base.mako"/>
<%namespace file="/message.mako" import="render_msg" />
<% from galaxy.util import nice_size %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Test Layout</title>
        <style type="text/css">
            body, html
            {
                margin: 0; padding: 0; height: 100%; overflow: hidden;
            }

            #content
            {
                position:absolute; left: 0; right: 0; bottom: 0; top: 0px; 
            }
        </style>
    </head>
    <body>
<!--    <div id="content"><iframe width="100%" height="100%" frameborder="0" src="http://prosight-cluster.kelleher.northwestern.edu/testing/galaxy_status_new.php/?jobId=${job.command_line.split('dataset_')[-1].split('.')[0]}&name=${job.command_line.split(' ')[-1]}"/></div>-->
<!--    <div id="content"><iframe width="100%" height="100%" frameborder="0" src="http://galaxy.kelleher.northwestern.edu/progress/?jobId=${job.command_line.split('dataset_')[-1].split('.')[0]}&name=${job.command_line.split(' ')[-1]}"/></div>-->
<!--    <div id="content"><iframe width="100%" height="100%" frameborder="0" src="https://portal.nrtdp.northwestern.edu/progress/?jobId=${job.command_line.split('dataset_')[-1].split('.')[0]}&name=${job.command_line.split(' ')[-1]}"/></div>-->
    <div id="content"><iframe width="100%" height="100%" frameborder="0" src="https://portal.nrtdp.northwestern.edu/progress/?jobId=${job.command_line.split('dataset_')[-1].split('.')[0] if "inputs" in job.command_line else job.command_line.split(' ')[8].split('/')[5]}"/></div>
    </body>
</html>

<style>
 enc.inherit {    
 border:border: 1px solid #bbb;
        padding: 15px;                 
        text-align: center;
        background-color: #eee;
    }
</style>  
