from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import vehicle, vehicle_group
from __init__ import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    #return "This is an example app"
    vehiclesdata = vehicle.query.all()
    vehiclesgroupdata = vehicle_group.query.all()
    return render_template("vehicle.html", vehicles = vehiclesdata, vehiclesgroup = vehiclesgroupdata)

@views.route('/vehicle_groupselect')
def vehicle_grouptest():
    #return "This is an example app"
    vehiclegroupdata = vehicle_group.query.all()
    return render_template("vehicle_group.html",vehicles_group = vehiclegroupdata)
    
@views.route('/about')
def about():
    return render_template('about.html')


def input():
     pass
 

@views.route("/insert",methods=['POST'])
def insert():
    if request.method == 'POST':
        vehicleid = request.form.get('vehicleid')
        vehicledescription = request.form.get('vehicledescription')
        vehicle_group = request.form.get('vehicle_group')
        vehiclestatus = request.form.get('vehiclestatus')
        newDescription = vehicle(vehicleid = vehicleid, vehicle_group = vehicle_group, vehicledescription=vehicledescription, vehiclestatus = vehiclestatus)
        db.session.add(newDescription)
        db.session.commit()
        flash('Vehicle created!',category='success')
    return redirect(url_for('views.index'))

#this is our update route where we are going to update our employee
@views.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = vehicle.query.get(request.form.get('vehicleid'))
 
        my_data.vehicleid = request.form['vehicleid']
        my_data.vehicledescription = request.form['vehicledescription']
        my_data.vehicle_group = request.form['vehicle_group']
        my_data.vehiclestatus = request.form['vehiclestatus']
 
        db.session.commit()
        flash("Vehicle updated successfully")
 
        return redirect(url_for('views.index'))
    
  
#This route is for deleting our employee
@views.route('/delete/<vehicleid>/', methods = ['GET', 'POST'])
def delete(vehicleid):
    my_data = vehicle.query.get(vehicleid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Vehicle Deleted Successfully")
 
    return redirect(url_for('views.index'))

@views.route("/insertgroup",methods=['POST'])
def insertgroup():
    if request.method == 'POST':
        vehicle_groupid = request.form.get('vehicle_groupid')
        vehicle_groupdescription = request.form.get('vehicle_groupdescription')
        vehicle_groupstatus = request.form.get('vehicle_groupstatus')
        newgroupDescription = vehicle_group(vehicle_groupid = vehicle_groupid, vehicle_groupdescription = vehicle_groupdescription, vehicle_groupstatus=vehicle_groupstatus)
        db.session.add(newgroupDescription)
        db.session.commit()
        flash('Vehicle group created!',category='success')
    return redirect(url_for('views.vehicle_grouptest')) 


@views.route('/updategroup', methods = ['GET', 'POST'])
def updategroup():
 
    if request.method == 'POST':
        my_groupdata = vehicle_group.query.get(request.form.get('vehicle_groupid'))
 
        my_groupdata.vehicle_groupid = request.form['vehicle_groupid']
        my_groupdata.vehicle_groupdescription = request.form['vehicle_groupdescription']
        my_groupdata.vehicle_groupstatus = request.form['vehicle_groupstatus']
      
 
        db.session.commit()
        flash("Group Updated Successfully")
 
        return redirect(url_for('views.vehicle_grouptest'))