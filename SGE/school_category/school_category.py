##############################################################################
#
# Copyright (c) 2013 Institut Obert de Catalunya (http://ioc.xtec.cat) 
#                    All Rights Reserved.
#                    Author: Isidre Guixà <iguixa@xtec.cat>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from osv import osv, fields

class school_course_category(osv.osv):
    """Categories of Courses"""
    _name = 'school.course.category'
    _columns = {
        'name': fields.char('Category', size=32, required=True),
        'parent_id': fields.many2one('school.course.category','Parent Category', help='Name of the parent category'),
        'child_ids': fields.one2many('school.course.category','parent_id','Child Categories'),
        'course_ids': fields.one2many('school.course','category_id','Courses'),
    }
    _constraints = [
        (osv.osv._check_recursion, 'Error ! You can not create recursive categories.', ['parent_id'])
    ]
school_course_category()

class school_course(osv.osv):
    """Courses with category"""
    _name = 'school.course'
    _inherit = 'school.course'
    _columns = {
        'category_id': fields.many2one('school.course.category','Category', help='Category of the course'),
    }
school_course()

