from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import vehicle, vehicle_group
from __init__ import db


views = Blueprint('views', __name__)


#main route for the vehicle form
@views.route('/')
def indexvehicle():
    vehiclesdata = vehicle.query.all()
    vehiclesgroupdata = vehicle_group.query.all()
    return render_template("vehicle.html", vehicles = vehiclesdata, vehiclesgroup = vehiclesgroupdata)


#main route for the vehicle_group form
@views.route('/vehicle_groupselect')
def indexgroup():
    vehiclegroupdata = vehicle_group.query.all()
    return render_template("vehicle_group.html",vehicles_group = vehiclegroupdata)
    
    
#main route for the about form
@views.route('/about')
def about():
    return render_template('about.html')

 
#this is our update route where we are going to add a vehicle
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
    return redirect(url_for('views.indexvehicle'))


#this is our update route where we are going to update our vehicle
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
 
        return redirect(url_for('views.indexvehicle'))
    
  
#This route is for deleting our vehicle
@views.route('/delete/<vehicleid>/', methods = ['GET', 'POST'])
def delete(vehicleid):
    my_data = vehicle.query.get(vehicleid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Vehicle Deleted Successfully")
 
    return redirect(url_for('views.indexvehicle'))


#This route is for deleting our vehicle_group
@views.route('/deletegroup/<vehicle_groupid>/', methods = ['GET', 'POST'])
def deletegroup(vehicle_groupid):
    my_data = vehicle_group.query.get(vehicle_groupid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Vehicle Deleted Successfully")
 
    return redirect(url_for('views.indexgroup'))


#this is our update route where we are going to add a vehicle_group
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
    return redirect(url_for('views.indexgroup')) 


#this is our update route where we are going to update our vehicle_group
@views.route('/updategroup', methods = ['GET', 'POST'])
def updategroup():
 
    if request.method == 'POST':
        my_groupdata = vehicle_group.query.get(request.form.get('vehicle_groupid'))
 
        my_groupdata.vehicle_groupid = request.form['vehicle_groupid']
        my_groupdata.vehicle_groupdescription = request.form['vehicle_groupdescription']
        my_groupdata.vehicle_groupstatus = request.form['vehicle_groupstatus']
      
 
        db.session.commit()
        flash("Group Updated Successfully")
 
        return redirect(url_for('views.indexgroup'))